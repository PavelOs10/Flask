from flask import Flask, jsonify, request

app = Flask(__name__)

storage = {}

@app.route('/add/<date>/<int:number>', methods=['POST'])
def add_expense(date, number):
    year = int(date[:4])
    month = int(date[4:6])
    storage.setdefault(year, {}).setdefault(month, {'total': 0})
    storage[year][month]['total'] += number

    return f"Расходы за {date} успешно добавлены."

@app.route('/calculate/<int:year>', methods=['GET'])
def calculate_year(year):
    if year not in storage:
        return f"Нет данных за {year}.", 404
    total_year_expenses = sum(month_data['total'] for month_data in storage[year].values())
    return jsonify({f"Затраты за {year}": total_year_expenses})

@app.route('/calculate/<int:year>/<int:month>', methods=['GET'])
def calculate_month(year, month):
    if year not in storage or month not in storage[year]:
        return f"Нет данных за {year}-{month}.", 404
    total_month_expenses = storage[year][month]['total']
    return jsonify({f"Затраты за {year}-{month}": total_month_expenses})


if __name__ == '__main__':
    app.run(debug=True)
