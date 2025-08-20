# app.py
from flask import Flask, render_template
from routes.credit import credit_bp  # Правильный импорт из папки routes

app = Flask(__name__)

# Регистрируем blueprint для кредитного калькулятора
app.register_blueprint(credit_bp)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cars')
def cars():
    return render_template('cars/cars.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

# Добавим маршруты для продажи автомобилей
@app.route('/sell/buyout')
def sell_buyout():
    return render_template('sell/sell_buyout.html')

@app.route('/sell/exchange')
def sell_exchange():
    return render_template('sell/sell_exchange.html')

@app.route('/sell/commission')
def sell_commission():
    return render_template('sell/sell_commission.html')

# Добавим маршрут для админ-панели
@app.route('/admin/login')
def admin_login():
    return render_template('admin/login.html')

if __name__ == '__main__':
    app.run(debug=True)