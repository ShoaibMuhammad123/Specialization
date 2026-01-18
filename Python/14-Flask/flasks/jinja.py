## Building URL dynamically
## Variable Rule
### Jinja 2 Template Engine

# Jinja2 Template Engine
'''
There are multiple ways , to read the datasource from the backend

1-{{}} expressions to print output in html
2-{%....%}  conditional statement , for loop , while loop etc
3-{#...#} Single line comment

'''


from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/submit',methods= ['GET','POST'])
def submit():
    if request.method=='POST':
        name = request.form['name']
        gender = request.form.get('gender')
        return f'Hello {name}'
    return render_template('form.html')        
    

## Variable Rule
@app.route('/success/<int:score>')
def success(score):
    if score > 50:
        res = 'pass'
    else:
        res = 'fail'
        
    return render_template('result.html',results = res)

## EXpression
@app.route('/successres/<int:score>')
def successres(score):
    if score > 50:
        res = 'pass'
    else:
        res = 'fail'
    
    # expression
    exp = {'score':score,'res':res}
    return render_template('resultexp.html',results = exp)
    
    
## Condition with if 
@app.route('/successif/<int:mark>')
def successif(mark):
    return render_template('resultif.html',marks = mark)


if __name__ =="__main__":
    app.run(debug=True)