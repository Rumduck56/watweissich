import time
import requests
import argparse

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select

parser = argparse.ArgumentParser()
parser.add_argument("--username", required=True)
parser.add_argument("--password", required=True)
args = parser.parse_args()
username = args.username
password = args.password

# driver = webdriver.Chrome('./chromedriver')

# driver.get('https://www.kicktipp.de/watweissich/profil/login')
# time.sleep(5)

# login = driver.find_element_by_id('kennung')
# login.send_keys(username)

# mypass = driver.find_element_by_id('passwort')
# mypass.send_keys(password)

# search_button = driver.find_element_by_name('submitbutton')
# search_button.click()

#driver.get('https://www.kicktipp.de/tipp469/tippuebersicht')

# Uwe's Tipps
# url = 'https://www.kicktipp.de/watweissich/tippuebersicht/tipper?spieltagIndex=7&ereignisIndex=8&rankingTeilnehmerId=24378486'
url = 'https://www.kicktipp.de/watweissich/tippuebersicht?&spieltagIndex=9'
login_url = "https://www.kicktipp.de/watweissich/profil/loginaction"

form_data = {
    "kennung": username,
    "passwort": password,
    "submitbutton": "Anmelden",
    "_charset_": "UTF-8"
}

headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Origin':
    'https://www.kicktipp.de',
    'Referer':
    'https://www.kicktipp.de/watweissich/profil/login',
    "Accept":
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}

# neue = driver.find_element_by_class_name('tablewrapper')

# print(neue.text)

#was nicht funktioniert - zwar keine Fehlermeldung, aber Daten werden wohl nicht vollständig geladen
with requests.Session() as c:
    c.get("https://www.kicktipp.de/")
    c.get("https://www.kicktipp.de/info/profil/login")
    r = c.post(login_url, data=form_data)
    # logged in
    page: requests.Response = c.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup)
