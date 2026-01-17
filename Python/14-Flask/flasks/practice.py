from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def Home():
    return '<h1>Welcome to Home</h1>'


@app.route('/portfolio',methods=['GET'])
def portfolio():
    return render_template('portfolio.html')


@app.route('/form',methods=['GET','POST'])
def form():
    if request.method =='POST':
        name = request.form.get('name')  
        gender = request.form.get('gender')  
        return f'Hellow {name} are you {gender}!'
        
    return render_template('form.html')


if __name__=='__main__':
    app.run(debug=True)