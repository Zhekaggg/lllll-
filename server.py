from flask import Flask, g, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_basicauth import BasicAuth
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
 # Change this to a secure password
app.config['SECRET_KEY'] = 'ijijiejdijedekd'  # Change this to a secure secret key
db = SQLAlchemy(app)
basic_auth = BasicAuth(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(50))
    full_name = db.Column(db.String(100))
    position = db.Column(db.String(50))
    work_schedule = db.Column(db.String(50))
    salary = db.Column(db.Float)
    currency = db.Column(db.String(50))
    education = db.Column(db.String(100))
    start_date = db.Column(db.Date)
    is_admin = db.Column(db.Boolean, default=False)

class AdminEmployee(Employee):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_admin = True


        

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = Employee.query.filter_by(username=username, password=password).first()

        if user:
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid credentials')

    return render_template('login.html', error=None)

# Add employee route
@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    admin_usernames = ['AL0', 'AL01', 'AL02']
    if 'logged_in' in session and session['logged_in']:
        if session['username'] in admin_usernames:  # Проверка, является ли пользователь AL0
            if request.method == 'POST':
                # Ваш код для добавления сотрудника
                username = request.form['username']
                password = request.form['password']
                full_name = request.form['full_name']
                position = request.form['position']
                work_schedule = request.form['work_schedule']
                salary = float(request.form['salary'])
                currency = request.form['currency']
                education = request.form['education']
                start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d')

                employee = Employee(
                    username = username,
                    password = password,
                    full_name=full_name,
                    position=position,
                    work_schedule=work_schedule,
                    salary=salary,
                    currency=currency,
                    education=education,
                    start_date=start_date
                )

                db.session.add(employee)
                db.session.commit()

                return redirect(url_for('index'))

            return render_template('add_employee.html')
        else:
            return redirect(url_for('index', error='no_permission'))

    else:
        return redirect(url_for('login'))
    
# Добавьте этот код после маршрута /add_employee
# Добавьте этот код после маршрута /add_employee
@app.route('/delete_employee/<int:employee_id>', methods=['POST'])
def delete_employee(employee_id):
    admin_usernames = ['AL0', 'AL01', 'AL02']
    if 'logged_in' in session and session['logged_in'] and session['username'] in admin_usernames:
        if request.method == 'POST':
            employee = Employee.query.get_or_404(employee_id)
            db.session.delete(employee)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return "Неверный метод запроса для удаления работника."
    else:
        return "У вас нет прав для удаления работника."

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))

@app.route('/')
def index():
    employees = Employee.query.all()
    admin_usernames = ['AL0', 'AL01', 'AL02']
    is_admin = 'logged_in' in session and session['logged_in'] and session['username'] in admin_usernames
    error = request.args.get('error')
    return render_template('index.html', employees=employees, is_admin=is_admin, error=error)


if __name__ == '__main__':
    app.run(debug=True)