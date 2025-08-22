from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.database import db, Admin

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/admin/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        admin = Admin.query.filter_by(username=username).first()

        if admin and admin.check_password(password):
            session['admin_logged_in'] = True
            session['admin_username'] = username
            flash('Вы успешно вошли в систему!', 'success')
            return redirect(url_for('cars.cars_list'))
        else:
            flash('Неверные учетные данные!', 'error')

    return render_template('admin/login.html')


@admin_bp.route('/admin/logout')
def logout():
    session.pop('admin_logged_in', None)
    session.pop('admin_username', None)
    flash('Вы вышли из системы!', 'success')
    return redirect(url_for('cars.cars_list'))