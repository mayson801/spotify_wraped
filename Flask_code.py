from flask import Flask, render_template, redirect, request, session, make_response,session,redirect,jsonify
import requests
from spotipy_code import *
import authorise_keys

app = Flask(__name__)

app.secret_key = authorise_keys.app_secret_key



API_BASE = 'https://accounts.spotify.com'

# Make sure you add this to Redirect URIs in the setting of the application dashboard
REDIRECT_URI = "http://127.0.0.1:5000/api_callback"

SCOPE = 'playlist-modify-private,playlist-modify-public,user-top-read'

# Set this to True for testing but you probably want it set to False in production.
SHOW_DIALOG = True

@app.route("/")
def pass_to_home():
    return render_template('home.html')
@app.route("/index")
def pass_to_index():
    return render_template('index.html')

# authorization-code-flow Step 1. Have your application request authorization;
# the user logs in and authorizes access
@app.route("/verify")
def verify():
    auth_url = f'{API_BASE}/authorize?client_id={authorise_keys.CLI_ID}&response_type=code&redirect_uri={REDIRECT_URI}&scope={SCOPE}&show_dialog={SHOW_DIALOG}'
    print(auth_url)
    return redirect(auth_url)
# authorization-code-flow Step 2.
# Have your application request refresh and access tokens;
# Spotify returns access and refresh tokens
@app.route("/api_callback")
def api_callback():
    session.clear()
    code = request.args.get('code')

    auth_token_url = f"{API_BASE}/api/token"
    res = requests.post(auth_token_url, data={
        "grant_type":"authorization_code",
        "code":code,
        "redirect_uri":"http://127.0.0.1:5000/api_callback",
        "client_id":authorise_keys.CLI_ID,
        "client_secret":authorise_keys.CLI_SEC
        })

    res_body = res.json()
    session["toke"] = res_body.get("access_token")

    #redirects to loading which is just an empty html that says loading
    #this is so user can't press login multiple time which would cause multiple graph.html to be loaded which is a slow process
    return redirect("loading")
# authorization-code-flow Step 3.
# Use the access token to access the Spotify Web API;
# Spotify returns requested data
@app.route("/loading")
def loading():
    return render_template("loading.html")

#@app.route("/load_data")
#def load_data():
 #   sp = spotipy.Spotify(auth=session['toke'])
  #  print (sp)
   # session["json_data"] = main(sp)
    #with open('test_json.txt') as json_file:
     #   data = json.load(json_file)
   # return redirect("graph")

@app.route("/graph")
def pass_to_graph():
    sp = spotipy.Spotify(auth=session['toke'])
    json_data = main(sp)
    return render_template("graph.html", data=json_data)

if __name__ == "__main__":
    app.run(debug=True)