from flask import Blueprint, abort, jsonify, render_template
import requests
from news_model import News
from datetime import date, timedelta

news_blueprint = Blueprint('news', __name__)

@news_blueprint.route("/")
def news_results_page():
    results = []
    response = requests.get(f'https://newsapi.org/v2/everything?q=olympics&from={date.today() - timedelta(days = 1)}&sortBy=publishedAt&apiKey=e33a9e25f48d47e88a26889cfe9318e7')
    if response.status_code != 200:
        abort(response.status_code, 'Something wrong')
    response = response.json()
    for news in response['articles']:
        if news['source']['name'] != '[Removed]' and news['title'] != '[Removed]' and news['urlToImage'] != '[Removed]' and news['urlToImage'] and news['publishedAt'] != '[Removed]'  and news['url'] != '[Removed]':                
            n = News(source=news['source']['name'], title=news['title'], urlToImage=news['urlToImage'], publishedAt=str(date.today()), url=news['url'])
            results.append(n)
    return render_template('news_page.html', news = results)