// static/js/script.js
// Функции для кредитного калькулятора (можно вынести сюда из HTML)
function calculatePayment() {
    const price = parseInt(document.getElementById('price').value);
    const initialPercent = parseInt(document.getElementById('initialPayment').value);
    const period = parseInt(document.getElementById('period').value);

    const loanAmount = price * (1 - initialPercent/100);
    const monthlyRate = 8.5 / 12 / 100;
    const monthlyPayment = loanAmount * (monthlyRate * Math.pow(1 + monthlyRate, period)) / (Math.pow(1 + monthlyRate, period) - 1);

    document.getElementById('monthlyPayment').textContent = Math.round(monthlyPayment).toLocaleString('ru-RU') + ' ₽';
}

// Инициализация при загрузке страницы
document.addEventListener('DOMContentLoaded', function() {
    // Синхронизация полей калькулятора
    const syncInputs = (inputId, rangeId) => {
        const input = document.getElementById(inputId);
        const range = document.getElementById(rangeId);

        if (input && range) {
            input.addEventListener('input', () => range.value = input.value);
            range.addEventListener('input', () => input.value = range.value);
        }
    };

    syncInputs('price', 'priceRange');
    syncInputs('initialPayment', 'initialPaymentRange');
    syncInputs('period', 'periodRange');

    // Первоначальный расчет если есть калькулятор
    if (document.getElementById('monthlyPayment')) {
        calculatePayment();
    }
});