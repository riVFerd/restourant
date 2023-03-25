import bs4
import requests
from bs4 import BeautifulSoup
from flask import render_template, Flask
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service

url = "https://www.spacex.com/launches/"

# using requests + BeautifulSoup
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# req = requests.get(url, headers=headers)
# soup = BeautifulSoup(req.text, 'html.parser')
#
# launches = soup.select('#items > div.item')
# for launch in launches:
#     print(launch.select_one('.date').text)
#     print(launch.select_one('.label').text)

# using selenium + BeautifulSoup
# driver = webdriver.Chrome('./chromedriver')
# driver.get(url)
# sleep(5)
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
#
# launches = soup.select('#items > div.item')
# for launch in launches:
#     print(launch.select_one('.date').text)
#     print(launch.select_one('.label').text)

app = Flask(__name__)


@app.route('/map')
def map():
    return render_template('prac_map.html')


if __name__ == '__main__':
    app.run(debug=True)
