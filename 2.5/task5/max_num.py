from flask import Flask, jsonify
import re

app = Flask(__name__)


@app.route('/max_number/<path:numbers>', methods=['GET'])
def max_number(numbers):
    num_list = numbers.split('/')
    try:
        valid_numbers = [float(num) for num in num_list if re.match(r'^-?\d+(\.\d+)?$', num)]

        if not valid_numbers:
            return "Ошибка: все переданные значения некорректны", 400

        max_number = max(valid_numbers)
        return f"Максимальное число: {max_number}"

    except ValueError:
        return "Ошибка: все переданные значения должны быть числами", 400


if __name__ == '__main__':
    app.run(debug=True)
