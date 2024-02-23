from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project_management.db'
app.config['SECRET_KEY'] = 'secret_key'
db = SQLAlchemy(app)
login_manager = LoginManager(app)

class Employee(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    role = db.Column(db.String(100))

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    contact_details = db.Column(db.String(100))
    address = db.Column(db.String(100))
    website_name = db.Column(db.String(100))

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_code = db.Column(db.String(100))
    project_name = db.Column(db.String(100))
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    project_members = db.Column(db.String(100))

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    task_name = db.Column(db.String(100))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    task_members = db.Column(db.String(100))

class TimeLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    description = db.Column(db.String(100))

@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = Employee.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                login_user(user)
                return redirect(url_for('dashboard'))
        flash('Invalid email or password')
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/add_employee', methods=['GET', 'POST'])


def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        email = request.
class Employee:
    def __init__(self, emp_id, name, email, role):
        self.emp_id = emp_id
        self.name = name
        self.email = email
        self.role = role

    def update_details(self, name=None, email=None, role=None):
        if name:
            self.name = name
        if email:
            self.email = email
        if role:
            self.role = role
class Attendance:
    def __init__(self, emp_id, date, in_time=None, out_time=None):
        self.emp_id = emp_id
        self.date = date
        self.in_time = in_time
        self.out_time = out_time

    def mark_attendance(self, in_time, out_time=None):
        self.in_time = in_time
        self.out_time = out_time
class Leave:
    def __init__(self, emp_id, start_date, end_date, status='Pending'):
        self.emp_id = emp_id
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

    def approve_leave(self):
        self.status = 'Approved'

    def disapprove_leave(self):
        self.status = 'Disapproved'
class Payroll:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

    def calculate_salary(self):
        # Add your salary calculation logic here
        pass

    def generate_payslip(self):
        # Add code to generate payslip
        pass
class ReportGenerator:
    @staticmethod
    def generate_employee_list(employees):
        for emp in employees:
            print(emp.name, emp.email, emp.role)
