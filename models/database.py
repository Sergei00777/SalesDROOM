from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    mileage = db.Column(db.Integer)
    fuel_type = db.Column(db.String(20))  # Бензин, Дизель, Электро
    transmission = db.Column(db.String(20))  # МКПП, АКПП
    image = db.Column(db.String(120))  # Путь к фото: /static/images/cars/...
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class SellRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), nullable=False)  # 'buyout', 'exchange', 'commission'

    # Общие поля
    brand = db.Column(db.String(50))
    model = db.Column(db.String(50))
    year = db.Column(db.Integer)
    mileage = db.Column(db.Integer)
    condition = db.Column(db.String(20))  # Отличное, Хорошее и т.д.
    price = db.Column(db.Integer)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100))
    message = db.Column(db.Text)

    # Только для обмена
    desired_car = db.Column(db.String(100))
    exchange_budget = db.Column(db.Integer)  # Доплата

    # Только для комиссии
    photo_paths = db.Column(db.Text)  # JSON или строка: "photo1.jpg,photo2.jpg"

    created_at = db.Column(db.DateTime, default=datetime.utcnow)