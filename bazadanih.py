from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    position = db.Column(db.String(100))
    work_schedule = db.Column(db.String(50))
    salary = db.Column(db.Integer)
    education = db.Column(db.String(100))
    start_date = db.Column(db.DateTime)

# Убедимся, что контекст приложения устанавливается правильно
with app.app_context():
    db.create_all()

# Добавление данных в базу
employee_data = [
    {"full_name": "Рашид", "position": "Продавец", "work_schedule": "2/2, смены с 6:00 до 21:00",
     "salary": 5000, "education": "Среднее не полное", "start_date": datetime(1903, 10, 29)},

    {"full_name": "Алишер Метрясов Рубеков", "position": "Стажер", "work_schedule": "2/2, смены с 6:00 до 21:00",
     "salary": 500, "education": "Отсутствует", "start_date": datetime(1903, 10, 29)},
    # Добавьте остальные данные здесь
]

with app.app_context():
    for data in employee_data:
        employee = Employee(
            full_name=data['full_name'],
            position=data['position'],
            work_schedule=data['work_schedule'],
            salary=data['salary'],
            education=data['education'],
            start_date=data['start_date']
        )
        db.session.add(employee)

        db.session.commit()