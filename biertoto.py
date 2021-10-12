import time
import requests
import argparse

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select

# der ganze argparse Spass hier ist damit man einfach ueber die command line den username und password uebergeben kann
# ```python biertoto.py --username <dein username> --password <dein password>`
parser = argparse.ArgumentParser()
parser.add_argument("--username", required=True)
parser.add_argument("--password", required=True)
args = parser.parse_args()
username = args.username
password = args.password

# hab ich auskommentiert fuer mein testen, kannste wieder hinzufuegen
# driver = webdriver.Chrome('./chromedriver')
# driver.get('https://www.kicktipp.de/watweissich/profil/login')
# time.sleep(5)
# login = driver.find_element_by_id('kennung')
# login.send_keys(username)
# mypass = driver.find_element_by_id('passwort')
# mypass.send_keys(password)
# search_button = driver.find_element_by_name('submitbutton')
# search_button.click()
# driver.get('https://www.kicktipp.de/tipp469/tippuebersicht')

# Uwe's Tipps
# url = 'https://www.kicktipp.de/watweissich/tippuebersicht/tipper?spieltagIndex=7&ereignisIndex=8&rankingTeilnehmerId=24378486'
# ich hab als URL einfach einen Spieltag angegeben
url = 'https://www.kicktipp.de/watweissich/tippuebersicht?&spieltagIndex=9'
# Das hier ist die Login URL
login_url = "https://www.kicktipp.de/watweissich/profil/loginaction"

# Und hier sind die login daten die mitgeschickt werden (hier wird das password und der username gesetzt von der command line)
form_data = {
    "kennung": username,
    "passwort": password,
    "submitbutton": "Anmelden",
    "_charset_": "UTF-8"
}

# header muss man wohl nicht setzen fuer den request, mach ich aber einfach mal... Irgendwie netter
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
# initial war die Anmeldung nicht in den requests mit drin, bei selenium oben schon, aber nicht fuer den requests
# wir nutzten hier eine requests session, damit nach der Anmeldung auch die cookies mit uebertragen werden bei den folgenden Requests
with requests.Session() as c:
    c.get("https://www.kicktipp.de/")
    c.get("https://www.kicktipp.de/info/profil/login")
    r = c.post(login_url, data=form_data, headers=headers)
    # jetzt sind wir logged in und alle weiteren requests haben dann auch die daten
    page: requests.Response = c.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup)
