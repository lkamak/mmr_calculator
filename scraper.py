import requests
from bs4 import BeautifulSoup

url = "https://red.op.lol/summoner/4/na/longandgirthy"
url2 = "https://pp.lolalytics.com/match/5/na/4006668249/"
data = requests.get(url2)
soup = BeautifulSoup(data.text, "html.parser")

print(soup)