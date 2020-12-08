from flask import Flask
from flask import render_template
from erm import *

app = Flask(__name__)
@app.route("/")
def pass_to_index():
    data= get_all_data()
    #data=get_test()
    print(data)
    return render_template('index.html',value=data)

if __name__ == "__main__":
    app.run()

