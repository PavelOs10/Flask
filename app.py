from flask import Flask, render_template

app = Flask(__name__)

page_view_count = 0

@app.route("/")
def home():
    global page_view_count
    page_view_count += 1
    return render_template("index.html")

@app.route("/views")
def views():
    return f"Главная страница была открыта {page_view_count} раз(а)."

if __name__ == "__main__":
    app.run(debug=True)
