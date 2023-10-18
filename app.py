from flask import Flask
from datetime import date

app = Flask(__name__)

# Приймаємо поточну дату
today = date.today()

@app.route('/')
def current_date():
    return f"<p>Поточна дата: {today}</p>"

if __name__ == '__main__':
    app.run()