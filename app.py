from flask import Flask, render_template, url_for, flash
from employee import employee_data
from forms import Signup_Form, Login_Form

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')
@app.route('/contact')
def contact():
    return render_template('contact.html',title='Contact')

@app.route('/recommended')
def recommend():
    return render_template('recommend.html',title='Book Store')

@app.route('/employees')
def employees():
    return render_template('employees.html', title='Employees', Employee_data=employee_data)

@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = Signup_Form
    if form.validate_on_submit():
        return flash('Submitted')
    return render_template('signup.html', title='Signup')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login_Form
    username = form.username.username
    
    if(username == '_samarth_'):
        return 'Correct'
    return render_template('login.html', title='Login')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', title='Dashboard')

if __name__ =='__main__':
    app.run(debug=True)