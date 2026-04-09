import requests
from bs4 import BeautifulSoup

URL = "https://debales.ai"

def get_data():
    try:
        res = requests.get(URL)
        soup = BeautifulSoup(res.text, "html.parser")
        return soup.get_text()
    except:
        return "Sample Debales AI content"
