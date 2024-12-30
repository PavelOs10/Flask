import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/head_file/<int:size>/<path:relative_path>', methods=['GET'])
def preview_file(size, relative_path):
    try:
        abs_path = os.path.abspath(relative_path)
        if not os.path.exists(abs_path) or not os.path.isfile(abs_path):
            return f"Ошибка: файл по пути {abs_path} не найден.", 404
        with open(abs_path, 'r', encoding='utf-8') as file:
            result_text = file.read(size)
        result_size = len(result_text)
        response = f"<b>{abs_path}</b> {result_size}<br>{result_text}"
        return response

    except Exception as e:
        return f"Ошибка: {str(e)}", 500


if __name__ == '__main__':
    app.run(debug=True)
