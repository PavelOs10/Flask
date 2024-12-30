from flask import Flask
from datetime import datetime

app = Flask(__name__)

weekdays = (
    "понедельника",  # 0
    "вторника",      # 1
    "среды",         # 2
    "четверга",      # 3
    "пятницы",       # 4
    "субботы",       # 5
    "воскресенья"    # 6
)

@app.route('/hello-world/<name>')
def hello_world(name):
    current_weekday = datetime.today().weekday()
    return f"Привет, {name}. Хорошего {weekdays[current_weekday]}!"

if __name__ == "__main__":
    app.run(debug=True)
