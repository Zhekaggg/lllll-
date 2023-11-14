from flask import Flask, render_template, request, redirect, url_for
from flask_basicauth import BasicAuth
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = 'adminpassword'
basic_auth = BasicAuth(app)

# Настройки базы данных SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Модель для хранения информации о пользователях
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

# Создание таблицы в базе данных

# Роут для главной страницы
@app.route('/')
def index():
    return render_template('index.html')

# Роут для страницы регистрации
@app.route('/register', methods=['GET', 'POST'])
@basic_auth.required  # Требование аутентификации для доступа к регистрации
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Проверка, что пароли совпадают
        if password != confirm_password:
            return render_template('register.html', error='Пароли не совпадают')

        # Создание нового пользователя
        new_user = User(first_name=first_name, last_name=last_name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html')

# Роут для страницы входа
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']

        # Поиск пользователя в базе данных
        user = User.query.filter_by(first_name=first_name, last_name=last_name, email=email, password=password).first()

        if user:
            return render_template('dashboard.html', user=user)
        else:
            return render_template('login.html', error='Неверный email или пароль')

    return render_template('login.html')

if __name__ == '__main__':
    # Перемещаем db.create_all() сюда
    
    app.run(debug=True)
