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
    {"full_name": "Рашид",
     "position": "Продавец",
      "work_schedule": "2/2, смены с 6:00 до 21:00",
     "salary": 5000,
      "education": "Среднее не полное",
      "start_date": datetime(1903, 10, 29)},

    {"full_name": "Алишер Метрясов Рубеков",
     "position": "Стажер",
      "work_schedule": "2/2, смены с 6:00 до 21:00",
     "salary": 500, 
     "education": "Отсутствует", 
     "start_date": datetime(1903, 10, 29)},

    {"full_name": "Ратмир Скала Папович",
     "position": " Охранник",
      "work_schedule": "5/2, смены с 1:00 до 22:00",
     "salary": 2006,
     "education": "Низшее",
      "start_date": datetime(1, 1, 1)},

    {"full_name": "Ролан Алпысбаев Курагович",
     "position": "Охранник",
      "work_schedule": "5/2, смены с 1:00 до 22:00",
     "salary": 2007 VEF (боливар),
     "education": "Пацанское-нисшее",
      "start_date": datetime(98, 21, 12)},

    {"full_name": "Дильназ Кенжалиева Муратовна",
     "position": "Уборщик",
      "work_schedule": "7/0, смены с 8:00 до 1:00",
     "salary": 6 VEF (боливар),
     "education": "Высшее",
      "start_date": datetime(14 июня 5672 года)},
    
    {"full_name": "Светлана Иванова",
     "position": "мЬл Бухгалтер",
      "work_schedule": "5/2, смены с 9:00 до 18:00",
     "salary": 700 VEF (боливар),
     "education": "Высшее",
      "start_date": datetime(3 апреля 2022 года)},

    {"full_name": "Максим Петров",
     "position": "Менеджер по закупкам",
      "work_schedule": "5/2, смены с 10:00 до 19:00",
     "salary": 550 VEF (боливар),
     "education": "Среднее",
      "start_date": datetime(Среднее)},

    {"full_name": "Анна Смирнова",
     "position": "Продавец-консультант",
      "work_schedule": "6/1, смены с 8:00 до 16:00",
     "salary": 400 VEF (боливар),
     "education": "Среднее специальное",
      "start_date": datetime(20 июля 2019 года)},

    {"full_name": "Иван Чернов",
     "position": "Разнорабочий",
      "work_schedule": "5/2, смены с 7:00 до 16:00",
     "salary": 550 VEF (боливар),
     "education": "Среднее профессиональное",
      "start_date": datetime(20 июня 2021 года)},

    {"full_name": "Семенович Кузнецов",
     "position": "Менеджер по закупкам",
      "work_schedule": "5/2, смены с 10:00 до 19:00",
     "salary": 800 VEF (боливар),
     "education": "Высшее",
      "start_date": datetime(15 марта 2015 года)},

    {"full_name": "Анна Павлова",
     "position": "Кассир",
      "work_schedule": "5/2, смены с 9:00 до 18:00",
     "salary": 300 VEF (боливар),
     "education": "Среднее",
      "start_date": datetime(10 декабря 2020 года)},

    {"full_name": "Лариса Сергеевна Иванова",
     "position": "Продавец",
      "work_schedule": "2/2, смены с 7:00 до 16:00",
     "salary": 450 VEF (боливар),
     "education": "Среднее",
      "start_date": datetime(25 ноября 2022 года)},

    {"full_name": "Владимир Михайлович Семенов",
     "position": "Менеджер по продажам",
      "work_schedule": "5/2, смены с 9:00 до 18:00",
     "salary": 600 VEF (боливар),
     "education": "Высшее",
      "start_date": datetime(10 августа 2021 года)},

    {"full_name": "Елена Анатольевна Павлова",
     "position": "Кассир",
      "work_schedule": "5/2, смены с 8:00 до 17:00",
     "salary": 350 VEF (боливар),
     "education": "Среднее",
      "start_date": datetime(5 сентября 2020 года)},

    {"full_name": "Алексей Игоревич Кузнецов",
     "position": "Охранник",
      "work_schedule": "5/2, смены с 1:00 до 22:00",
     "salary": 210 VEF (боливар),
     "education": "Среднее",
      "start_date": datetime(7 марта 2022 года)},

    {"full_name": "Ольга Николаевна Лебедева",
     "position": "Уборщик",
      "work_schedule": "7/0, смены с 8:00 до 1:00",
     "salary": 420 VEF (боливар),
     "education": "Среднее профессиональное",
      "start_date": datetime(12 апреля 2018 года)},

    {"full_name": "Денис Викторович Попов",
     "position": "Менеджер по закупкам",
      "work_schedule": "5/2, смены с 10:00 до 19:00",
     "salary": 700 VEF (боливар),
     "education": "Высшее",
      "start_date": datetime(8 июля 2019 года)},

    {"full_name": "Екатерина Александровна Смирнова",
     "position": "Продавец-консультант",
      "work_schedule": "6/1, смены с 9:00 до 17:00",
     "salary": 380 VEF (боливар),
     "education": "Среднее специальное",
      "start_date": datetime(23 мая 2020 года)},

    {"full_name": "Данииил Зайцев ",
     "position": "Разнорабочий",
      "work_schedule": "5/2, смены с 8:00 до 17:00",
     "salary": 460 VEF (боливар),
     "education": "Среднее профессиональное",
      "start_date": datetime(17 июля 2021 года)},

    {"full_name": "Елена Александровна Козлова",
     "position": "Менеджер по маркетингу",
      "work_schedule": "5/2, смены с 9:00 до 18:00",
     "salary": 650 VEF (боливар),
     "education": "Высшее",
      "start_date": datetime(14 марта 2017 года)},

    {"full_name": "Эльдар салихов ",
     "position": "бухгалтер ",
      "work_schedule": "1/12, с 13:00 до 14:00",
     "salary": 10000 USD ,
     "education": "высшее да",
      "start_date": datetime(21 год до большого взрыва )},

    {"full_name": "Жаслан Курмашен да ",
     "position": "эректор немец ",
      "work_schedule": "1/12, с 13:00 до 14:00",
     "salary": 10000 USD,
     "education": "высшее немецкое  ",
      "start_date": datetime(21 год до большого взрыва )},

    {"full_name": "Козлов Влад ",
     "position": "эректор немец ",
      "work_schedule": "1/12, с 13:00 до 14:00",
     "salary": 10000 USD,
     "education": "высшее немецкое  ",
      "start_date": datetime(21 год до большого взрыва)}
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