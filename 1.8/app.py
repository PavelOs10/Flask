from flask import Flask, render_template
import random
import datetime
import os
import re
import chardet

app = Flask(__name__)

visits = 0
car = ["Chevrolet", "Renault", "Ford", "Lada"]
cat = ["корниш-рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин"]
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')
def get_words_from_file(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
    detected = chardet.detect(raw_data)
    encoding = detected['encoding']
    with open(file_path, 'r', encoding=encoding) as file:
        text = file.read()
    words = re.findall(r'\b\w+\b', text)
    return words

words_list = get_words_from_file(BOOK_FILE)

@app.route("/hello_world")
def hello_world():
    return "привет мир!"

@app.route("/cars")
def cars():
    return ", ".join(car)

@app.route("/cats")
def cats():
    return random.choice(cat)

@app.route("/get_time/now")
def now():
    return f"Точное время {datetime.datetime.now()}"

@app.route("/get_time/future")
def future():
    current_time = datetime.datetime.now()
    time_after_hour = current_time + datetime.timedelta(hours=1)
    return f"Точное время через час: {time_after_hour.strftime('%Y-%m-%d %H:%M:%S')}"

@app.route("/get_random_word")
def get_random_word():
    random_word = random.choice(words_list)
    return f"Случайное слово: {random_word}"

@app.route("/counter")
def counter():
    global visits
    visits += 1
    return f"Страница была открыта {visits} раз(а)"

if __name__ == "__main__":
    app.run(debug=True)
