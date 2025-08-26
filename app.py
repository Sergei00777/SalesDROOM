from flask import Flask, render_template
from models.database import db, Admin
from routes.credit import credit_bp
from routes.cars import cars_bp
from routes.admin import admin_bp
import os

app = Flask(__name__)

# Загрузка конфигурации
app.config.from_pyfile('config.py')

# Создаем папку instance если ее нет
os.makedirs(os.path.join(app.root_path, 'instance'), exist_ok=True)

# Инициализация базы данных
db.init_app(app)

# Регистрируем blueprints
app.register_blueprint(credit_bp)
app.register_blueprint(cars_bp)
app.register_blueprint(admin_bp)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

# Маршруты для продажи автомобилей
@app.route('/sell/buyout')
def sell_buyout():
    return render_template('sell/sell_buyout.html')

@app.route('/sell/exchange')
def sell_exchange():
    return render_template('sell/sell_exchange.html')

@app.route('/sell/commission')
def sell_commission():
    return render_template('sell/sell_commission.html')

# В файле app.py добавляем новые маршруты
@app.route('/sell/parts')
def sell_parts():
    return render_template('sell/sell_parts.html')

@app.route('/sell/import')
def sell_import():
    return render_template('sell/sell_import.html')

# Функция для инициализации базы данных
def init_db():
    with app.app_context():
        db.create_all()
        # Создаем администратора
        admin = Admin.query.filter_by(username='СЕРГЕЙ').first()
        if not admin:
            admin = Admin(username='СЕРГЕЙ')
            admin.set_password('336996')
            db.session.add(admin)
            db.session.commit()
        print("База данных инициализирована, администратор создан")

# Инициализируем базу данных при запуске приложения
with app.app_context():
    init_db()

if __name__ == '__main__':
    print(f"Database URI: {app.config.get('SQLALCHEMY_DATABASE_URI')}")
    print(f"Instance path: {app.instance_path}")
    app.run(debug=True)