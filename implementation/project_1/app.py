from typing import final
from flask import Flask, render_template, request
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import requests

app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/plain_news', methods=['GET', 'POST'])
def plain_news():
    text = request.form['text_id']
    return render_template("output.html", plain_news = text)

@app.route('/news_article_link',  methods=['GET', 'POST'])
def link_to_content():
    article_link = request.form['article_id']
    ar           = requests.get(article_link)
    article = BeautifulSoup(ar.text,"lxml")
    if article.find(id="pcl-full-content") == None:
        return render_template("output.html", news = 'None')
    else:
        content = ""
        for para in article.find('div', id = "pcl-full-content").find_all("p"):
            content+=para.get_text()
        return render_template("output.html", news_content = content)

@app.route('/translate_news', methods=['GET', 'POST'])
def translate():
    text            = request.form['translate_text_id']
    language        = request.form['destination_language_id']
    translated_text = GoogleTranslator(source='auto', target=language).translate(text)
    return render_template("output.html", translated_news = translated_text)

@app.route('/summarize_news', methods=['GET', 'POST'])
def summarize_news():
    final_text = request.form['summarize_id']
    return render_template("page_1.html", ready_text = final_text)

@app.route('/categorize_news', methods=['GET', 'POST'])
def categorize_news():
    final_text = request.form['categorize_id']
    return render_template("page_1.html", ready_text = final_text)

if __name__ == '__main__':
	app.run(debug=True)
