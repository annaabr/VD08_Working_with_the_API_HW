from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    quote = get_random_quote()
    return render_template('index.html', quote=quote)

def get_random_quote():
    response = requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=ru")
    if response.status_code == 200:
        data = response.json()
        return data['quoteText'], data['quoteAuthor']
    return "Не удалось получить цитату", "Неизвестный автор"

if __name__ == '__main__':
    app.run(debug=True)