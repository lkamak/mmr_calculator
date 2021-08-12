import requests
from requests.api import options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


"""
These are the URLs I'm using in my requests. 
"""
DRIVER_PATH = '/Users/lkamakura/git/mmr_calculator/chromedriver'
lolalytics_url = "https://lolalytics.com/"
url = "https://red.op.lol/summoner/4/na/longandgirthy"
url2 = "https://pp.lolalytics.com/match/5/na/4006668249/"

"""
This block of code sets the options of my chromium driver. It must be headless so it isn't forced to run JavaScript.
Window size is 1920 by 1200
"""
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

"""
Here I create my driver object so I can navigate the pages withouth a graphical interface. 
"""
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://lolalytics.com/na/longandgirthy")
time.sleep(10)
# The xpath I get from the source page in chrome. I could use other ways to find this element, but it would be good to learn about xpaths
div = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[2]/div[3]/div[2]/div[2]/div[1]')

print(div.text)
print(driver.page_source)
driver.quit()