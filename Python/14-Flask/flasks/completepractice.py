from flask import Flask,render_template,request,redirect,url_for,jsonify

app = Flask(__name__)

@app.route('/')
def Welcome():
    return render_template('1_Home.html')


@app.route('/apply', methods=['GET', 'POST'])
def apply():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        course = request.form.get('course')

        exp = {
            'name': name,
            'age': age,
            'course': course
        }

        return render_template('3_applied.html', results=exp)

    return render_template('2_form.html')

@app.route('/four_success/<int:marks>')
def four_success(marks):
    return f'Your have passed the exam with {marks} marks'

@app.route('/four_fail/<int:marks>')
def four_fail(marks):
    return f'Your have failed the exam with {marks} marks'

## Dynamic url
@app.route('/testscore/<int:marks>')
def testscore(marks):
    if marks >50:
        return redirect(url_for('four_success',marks=marks))
    else:
        return redirect(url_for('four_fail',marks=marks))
    
        
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]


# API endpoint
@app.route("/api/users")
def get_users():
    return jsonify(users)

if __name__=='__main__':
    app.run(debug=True)