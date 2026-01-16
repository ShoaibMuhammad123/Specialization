from flask import Flask,render_template

"""

How we can integrate our html file with flask app itself, and we will see the functionality of render template (it is used 
for url redirecting)

"""

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<h1> Welcome to the home Screen </h1>"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
if __name__=='__main__':
    app.run(debug=True)