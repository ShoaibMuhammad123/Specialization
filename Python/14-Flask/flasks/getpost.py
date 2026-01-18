"""
Get and Post Request with Flask
"""

from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/success/<marks>')
def success(marks):
    return 'You have passed with marks' + marks if int(marks) >50 else 'You have fail with marks'+ marks
    
    
## For Get and POST both
@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name = request.form['name']
        gender = request.form['gender']
        return 'Hello {},{}'.format(gender,name)
    else:
        return render_template('form.html')
    

    
    
if __name__ =="__main__":
    app.run(debug=True)