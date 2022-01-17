import sys
import requests
import bs4
from funkce import vytvoreni_hlavicky, ulozeni_tabulky, ziskani_dat

csv_file = sys.argv[2]
url = sys.argv[1]
base_url = url.rsplit('/', 1)[0]

response = requests.get(url)
route_page = bs4.BeautifulSoup(response.text, "html.parser")

obce = route_page.main.find_all('td', {"class": "overflow_name"})
cisla_obce = route_page.main.find_all('td', {"class": "cislo"})

header = vytvoreni_hlavicky(base_url, cisla_obce)
csv_data = [header]

csv_data += ziskani_dat(base_url, obce, cisla_obce)

ulozeni_tabulky(csv_file, csv_data)