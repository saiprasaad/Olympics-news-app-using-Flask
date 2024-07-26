from flask import Blueprint, abort, jsonify, render_template
import requests
from news_model import News

news_blueprint = Blueprint('news', __name__)

@news_blueprint.route("/")
def news_results_page():
    results = []
    response = requests.get('https://newsapi.org/v2/everything?q=olympics&to=2024-06-26&sortBy=publishedAt&language=en&apiKey=e33a9e25f48d47e88a26889cfe9318e7')
    if response.status_code != 200:
        abort(response.status_code, 'Something wrong')
    response = response.json()
    for news in response['articles']:
        if news['source']['name'] != '[Removed]' and news['title'] != '[Removed]' and news['urlToImage'] != '[Removed]' and news['urlToImage'] and news['publishedAt'] != '[Removed]'  and news['url'] != '[Removed]':                
            n = News(source=news['source']['name'], title=news['title'], urlToImage=news['urlToImage'], publishedAt=news['publishedAt'], url=news['url'])
            results.append(n)
    return render_template('news_page.html', news = results)