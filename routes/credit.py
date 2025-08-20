
# routes/credit.py
from flask import Blueprint, render_template, request

credit_bp = Blueprint('credit', __name__)


@credit_bp.route('/credit')
def credit_calculator():
    # Получаем параметры из запроса, если они есть
    price = request.args.get('price', '', type=str)
    initial_payment = request.args.get('initial_payment', '', type=str)
    period = request.args.get('period', '', type=str)

    # Параметры по умолчанию для калькулятора
    default_price = 1000000
    default_initial_percent = 20
    default_period = 36

    # Рассчитываем пример платежа по умолчанию
    monthly_payment = calculate_credit_payment(default_price, default_initial_percent, default_period)

    return render_template('credit.html',
                           price=price,
                           initial_payment=initial_payment,
                           period=period,
                           monthly_payment=monthly_payment,
                           default_price=default_price,
                           default_initial_percent=default_initial_percent,
                           default_period=default_period)


def calculate_credit_payment(price, initial_percent, period_months):
    """
    Функция для расчета ежемесячного платежа
    Упрощенная формула аннуитетного платежа
    """
    try:
        loan_amount = price * (1 - initial_percent / 100)
        # Примерная процентная ставка (годовая)
        annual_rate = 8.5
        monthly_rate = annual_rate / 12 / 100

        if monthly_rate == 0:
            return loan_amount / period_months

        monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate) ** period_months) / (
                    (1 + monthly_rate) ** period_months - 1)
        return int(monthly_payment)
    except:
        return 0