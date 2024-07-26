from flask import Flask
from news_blueprint import news_blueprint

app = Flask(__name__)
app.register_blueprint(news_blueprint)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")