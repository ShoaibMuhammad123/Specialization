from flask import Flask


"""
    Creating instannce of WSGI.
"""

## WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Wel Come to the Screen, This is my first appllication using flask framework"

@app.route("/index")
def index():
    return "This is the index page."

## Entry Point 
if __name__ =="__main__":
    app.run(debug=True)      

