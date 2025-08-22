from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.database import db, Car, Admin
from functools import wraps
import os
from werkzeug.utils import secure_filename

cars_bp = Blueprint('cars', __name__)

# Настройки загрузки файлов
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
UPLOAD_FOLDER = 'static/images/cars'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Декоратор для проверки админских прав
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin.login'))
        return f(*args, **kwargs)

    return decorated_function


@cars_bp.route('/cars')
def cars_list():
    cars = Car.query.filter_by(is_active=True).all()
    return render_template('cars/cars.html', cars=cars)


@cars_bp.route('/car/<int:id>')
def car_detail(id):
    car = Car.query.get_or_404(id)
    return render_template('cars/car_detail.html', car=car)


@cars_bp.route('/cars/add', methods=['GET', 'POST'])
@admin_required
def add_car():
    if request.method == 'POST':
        try:
            # Создаем автомобиль
            car = Car(
                brand=request.form['brand'],
                model=request.form['model'],
                year=int(request.form['year']),
                price=int(request.form['price']),
                mileage=int(request.form['mileage']),
                body_type=request.form['body_type'],
                steering=request.form['steering'],
                engine_volume=request.form['engine_volume'],
                fuel_type=request.form['fuel_type'],
                power=request.form['power'],
                transmission=request.form['transmission'],
                drive=request.form['drive'],
                color=request.form['color'],
                vin=request.form.get('vin', ''),
                description=request.form.get('description', '')
            )

            # Обработка загрузки фото
            if 'image' in request.files:
                files = request.files.getlist('image')
                for i, file in enumerate(files):
                    if file and allowed_file(file.filename):
                        filename = secure_filename(file.filename)
                        # Сохраняем только первое фото для простоты
                        if i == 0:
                            file_path = os.path.join(UPLOAD_FOLDER, filename)
                            file.save(file_path)
                            car.image_path = f'/static/images/cars/{filename}'
                            break

            db.session.add(car)
            db.session.commit()
            flash('Автомобиль успешно добавлен!', 'success')
            return redirect(url_for('cars.cars_list'))

        except Exception as e:
            db.session.rollback()
            flash(f'Ошибка при добавлении автомобиля: {str(e)}', 'error')

    return render_template('admin/car_form.html', car=None)


@cars_bp.route('/cars/edit/<int:id>', methods=['GET', 'POST'])
@admin_required
def edit_car(id):
    car = Car.query.get_or_404(id)
    if request.method == 'POST':
        try:
            car.brand = request.form['brand']
            car.model = request.form['model']
            car.year = int(request.form['year'])
            car.price = int(request.form['price'])
            car.mileage = int(request.form['mileage'])
            car.body_type = request.form['body_type']
            car.steering = request.form['steering']
            car.engine_volume = request.form['engine_volume']
            car.fuel_type = request.form['fuel_type']
            car.power = request.form['power']
            car.transmission = request.form['transmission']
            car.drive = request.form['drive']
            car.color = request.form['color']
            car.vin = request.form.get('vin', '')
            car.description = request.form.get('description', '')

            # Обработка загрузки фото
            if 'image' in request.files:
                files = request.files.getlist('image')
                for i, file in enumerate(files):
                    if file and allowed_file(file.filename):
                        filename = secure_filename(file.filename)
                        if i == 0:  # Сохраняем только первое фото
                            file_path = os.path.join(UPLOAD_FOLDER, filename)
                            file.save(file_path)
                            car.image_path = f'/static/images/cars/{filename}'
                            break

            db.session.commit()
            flash('Автомобиль успешно обновлен!', 'success')
            return redirect(url_for('cars.car_detail', id=car.id))

        except Exception as e:
            db.session.rollback()
            flash(f'Ошибка при обновлении автомобиля: {str(e)}', 'error')

    return render_template('admin/car_form.html', car=car)


@cars_bp.route('/cars/delete/<int:id>')
@admin_required
def delete_car(id):
    car = Car.query.get_or_404(id)
    car.is_active = False
    db.session.commit()
    flash('Автомобиль удален!', 'success')
    return redirect(url_for('cars.cars_list'))