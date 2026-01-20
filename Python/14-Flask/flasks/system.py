from flask import Flask,render_template,request

app = Flask(__name__)

users = {
    'name':'shoaib',
    'age':'22',
    'course':'computer Science'
}


@app.route('/')
def login_page():
    return render_template('2_form.html')

@app.route('/handle_get')
def handle_get():
    if request.method=='GET':
        name = request.args['name']
        age = request.args['age']
    
    print(name,age)
    

@app.route('/handle_post', methods=['POST'])
def handle_post():
    name = request.form.get('name')
    age = request.form.get('age')
    course = request.form.get('course')

    print(name, age, course)
  

    if name == users['name'] and age == users['age']:
        return 'Welcome to the amazing app'
    else:
        return 'Invalid details'

@app.route('/update_data',methods=['PUT'])
def update_data():
    if request.method=='PUT':
        name_up = request.form.get('name')
        age_up = request.form.get('age')
        course_up = request.form.get('course')
        
        if name_up not in users['name']:
            users['name']=name_up
            users['age'] = age_up
            users['course']=course_up
        return f'updated name : {users["name"]} Age: {users['age']} and Course: {users['course']}'
    else:
        return 'Some thing is wrong'
               
if __name__=='__main__':
    app.run(debug=True)