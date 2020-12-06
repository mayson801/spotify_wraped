from flask import Flask
from flask import render_template
from erm import main


app = Flask(__name__)
@app.route("/")
def pass_to_index():

    return render_template('index.html')



if __name__ == "__main__":
    app.run()

