from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    position = db.Column(db.String(50))
    work_schedule = db.Column(db.String(50))
    salary = db.Column(db.Float)
    currency = db.Column(db.String(50))
    education = db.Column(db.String(100))
    start_date = db.Column(db.Date)

"""with app.app_context():
    db.create_all()

# Добавление данных в базу
employee_data = [
    {"full_name": "Рашид",
     "position": "Продавец",
      "work_schedule": "2/2, смены с 6:00 до 21:00",
     "salary": 5000 ,
     "currency": "VEF",
      "education": "Среднее не полное",
      "start_date": datetime(1903, 10, 29)},

    {"full_name": "Алишер Метрясов Рубеков",
     "position": "Стажер",
      "work_schedule": "2/2, смены с 6:00 до 21:00",
     "salary": 500, "currency": "VEF", 
     "education": "Отсутствует", 
     "start_date": datetime(1903, 10, 29)},

    {"full_name": "Ратмир Скала Папович",
     "position": " Охранник",
      "work_schedule": "5/2, смены с 1:00 до 22:00",
     "salary": 2006, "currency":"VEF",
     "education": "Низшее",
      "start_date": datetime(1, 1, 1)},

    {"full_name": "Ролан Алпысбаев Курагович",
     "position": "Охранник",
      "work_schedule": "5/2, смены с 1:00 до 22:00",
     "salary": 2007, "currency": "VEF" ,
     "education": "Пацанское-нисшее",
      "start_date": datetime(1588, 12, 21)},

    {"full_name": "Дильназ Кенжалиева Муратовна",
     "position": "Уборщик",
      "work_schedule": "7/0, смены с 8:00 до 1:00",
     "salary": 6 ,"currency":"VEF" ,
     "education": "Высшее",
      "start_date": datetime(1672, 6, 14)},
    
    {"full_name": "Светлана Иванова",
     "position": "мЬл Бухгалтер",
      "work_schedule": "5/2, смены с 9:00 до 18:00",
     "salary": 700 ,"currency":"VEF" ,
     "education": "Высшее",
      "start_date": datetime(2022, 4, 3)},

    {"full_name": "Максим Петров",
     "position": "Менеджер по закупкам",
      "work_schedule": "5/2, смены с 10:00 до 19:00",
     "salary": 550, "currency":"VEF" ,
     "education": "Среднее",
      "start_date": datetime(2021, 5, 15)},

    {"full_name": "Анна Смирнова",
     "position": "Продавец-консультант",
      "work_schedule": "6/1, смены с 8:00 до 16:00",
     "salary": 400, "currency":"VEF" ,
     "education": "Среднее специальное",
      "start_date": datetime(2019, 7, 20)},

    {"full_name": "Иван Чернов",
     "position": "Разнорабочий",
      "work_schedule": "5/2, смены с 7:00 до 16:00",
     "salary": 550,"currency": "VEF" ,
     "education": "Среднее профессиональное",
      "start_date": datetime(2021, 6, 20)},

    {"full_name": "Семенович Кузнецов",
     "position": "Менеджер по закупкам",
      "work_schedule": "5/2, смены с 10:00 до 19:00",
     "salary": 800, "currency":"VEF",
     "education": "Высшее",
      "start_date": datetime(2015, 3, 15)},

    {"full_name": "Анна Павлова",
     "position": "Кассир",
      "work_schedule": "5/2, смены с 9:00 до 18:00",
     "salary": 300,"currency": "VEF" ,
     "education": "Среднее",
      "start_date": datetime( 2020, 12, 10)},

    {"full_name": "Лариса Сергеевна Иванова",
     "position": "Продавец",
      "work_schedule": "2/2, смены с 7:00 до 16:00",
     "salary": 450,"currency": "VEF" ,
     "education": "Среднее",
      "start_date": datetime(2022, 11, 25)},

    {"full_name": "Владимир Михайлович Семенов",
     "position": "Менеджер по продажам",
      "work_schedule": "5/2, смены с 9:00 до 18:00",
     "salary": 600 ,"currency":"VEF" ,
     "education": "Высшее",
      "start_date": datetime(2021, 8,10)},

    {"full_name": "Елена Анатольевна Павлова",
     "position": "Кассир",
      "work_schedule": "5/2, смены с 8:00 до 17:00",
     "salary": 350,"currency": "VEF" ,
     "education": "Среднее",
      "start_date": datetime(2020, 9,5 )},

    {"full_name": "Алексей Игоревич Кузнецов",
     "position": "Охранник",
      "work_schedule": "5/2, смены с 1:00 до 22:00",
     "salary": 210,"currency": "VEF" ,
     "education": "Среднее",
      "start_date": datetime( 2022,3,7 )},

    {"full_name": "Ольга Николаевна Лебедева",
     "position": "Уборщик",
      "work_schedule": "7/0, смены с 8:00 до 1:00",
     "salary": 420,"currency": "VEF" ,
     "education": "Среднее профессиональное",
      "start_date": datetime( 2018,4,12)},

    {"full_name": "Денис Викторович Попов",
     "position": "Менеджер по закупкам",
      "work_schedule": "5/2, смены с 10:00 до 19:00",
     "salary": 700,"currency": "VEF" ,
     "education": "Высшее",
      "start_date": datetime( 2019,7,8)},

    {"full_name": "Екатерина Александровна Смирнова",
     "position": "Продавец-консультант",
      "work_schedule": "6/1, смены с 9:00 до 17:00",
     "salary": 380, "currency":"VEF" ,
     "education": "Среднее специальное",
      "start_date": datetime( 2020,5,23)},

    {"full_name": "Данииил Зайцев ",
     "position": "Разнорабочий",
      "work_schedule": "5/2, смены с 8:00 до 17:00",
     "salary": 460, "currency":"VEF" ,
     "education": "Среднее профессиональное",
      "start_date": datetime(  2021,7,17)},

    {"full_name": "Елена Александровна Козлова",
     "position": "Менеджер по маркетингу",
      "work_schedule": "5/2, смены с 9:00 до 18:00",
     "salary": 650,"currency": "VEF" ,
     "education": "Высшее",
      "start_date": datetime( 2017, 3,14)},

    {"full_name": "Эльдар салихов ",
     "position": "бухгалтер ",
      "work_schedule": "1/12, с 13:00 до 14:00",
     "salary": 10000,"currency": "USD" ,
     "education": "высшее да",
      "start_date": datetime(1 ,1,1)},

    {"full_name": "Жаслан Курмашен да ",
     "position": "эректор немец ",
      "work_schedule": "1/12, с 13:00 до 14:00",
     "salary": 10000,"currency": "USD",
     "education": "высшее немецкое  ",
      "start_date": datetime(1,1,1)},

    {"full_name": "Козлов Влад ",
     "position": "эректор немец ",
      "work_schedule": "1/12, с 13:00 до 14:00",
     "salary": 10000,"currency": "USD",
     "education": "высшее немецкое  ",
      "start_date": datetime(1,1,1)}
    # Добавьте остальные данные здесь
]

with app.app_context():
    for data in employee_data:
        employee = Employee(
            full_name=data['full_name'],
            position=data['position'],
            work_schedule=data['work_schedule'],
            salary=data['salary'],
            currency=data['currency'],
            education=data['education'],
            start_date=data['start_date']
        )
        db.session.add(employee)

        db.session.commit()"""

@app.route('/')
def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True)
