from flask import Flask, render_template, request
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import requests

app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template('index.html')

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
            return render_template("output.html", news = content)

        # news_text    = request.form['text_id']
        # source_text  = request.form['translate_text_id']
        # destination_language = request.form['destination_language_id']
        # if request.form.get('translate_button'):
        #     translate = GoogleTranslator(source='auto', target=destination_language).translate(news_text)
        #     return render_template("output.html", translate = translate)
        # else:
        #     return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True)
