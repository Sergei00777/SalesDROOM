from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100), nullable=False)  # Марка
    model = db.Column(db.String(100), nullable=False)  # Модель
    year = db.Column(db.Integer, nullable=False)  # Год выпуска
    price = db.Column(db.Integer, nullable=False)  # Цена
    mileage = db.Column(db.Integer, nullable=False)  # Пробег
    body_type = db.Column(db.String(50), nullable=False)  # Кузов
    steering = db.Column(db.String(50), nullable=False)  # Руль (левый/правый)
    engine_volume = db.Column(db.String(50), nullable=False)  # Двигатель (объем)
    fuel_type = db.Column(db.String(50), nullable=False)  # Тип топлива
    power = db.Column(db.String(50), nullable=False)  # Мощность (л.с.)
    transmission = db.Column(db.String(50), nullable=False)  # КПП
    drive = db.Column(db.String(50), nullable=False)  # Привод
    color = db.Column(db.String(50), nullable=False)  # Цвет
    vin = db.Column(db.String(100), nullable=True)  # VIN номер
    description = db.Column(db.Text, nullable=True)  # Описание
    image_path = db.Column(db.String(200), nullable=True)  # Путь к фото
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class SellRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    car_brand = db.Column(db.String(100), nullable=False)
    car_model = db.Column(db.String(100), nullable=False)
    car_year = db.Column(db.Integer, nullable=False)
    request_type = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='new')