import requests
import bs4
from unicodedata import normalize
import csv

UNICODE_FORM = "NFKC"

def vytvoreni_hlavicky(base_url,  cisla_obce):
    response = requests.get(base_url + "/" + cisla_obce[0].a["href"])
    sub_page = bs4.BeautifulSoup(response.text, "html.parser")
    all_tables = sub_page.find_all("table")
    radky_strany = all_tables[1].find_all("tr")[2:]
    radky_strany += all_tables[2].find_all("tr")[2:]

    header = ["code", "location", "registered", "envelopes", "valid"]
    for radek_strana in radky_strany:
        header.append(normalize(UNICODE_FORM, radek_strana.find_all("td")[1].text))
    return header

def ziskani_dat(base_url, obce, cisla_obce):
    data = []
    for obec, radek in zip(obce, cisla_obce):
        response = requests.get(base_url + "/" + radek.a["href"])
        sub_page = bs4.BeautifulSoup(response.text, "html.parser")
        all_tables = sub_page.find_all("table")

        # Sloupce 1-5
        table_data = all_tables[0].find_all("td")
        csv_radek = [
            radek.a.text,
            obec.text,
            normalize(UNICODE_FORM, table_data[3].text),
            normalize(UNICODE_FORM, table_data[4].text),
            normalize(UNICODE_FORM, table_data[7].text)
        ]

        # 6. kandidující strany
        radky_strany = all_tables[1].find_all("tr")[2:]
        radky_strany += all_tables[2].find_all("tr")[2:]

        for radek_strana in radky_strany:
            csv_radek.append(normalize(UNICODE_FORM, radek_strana.find_all("td")[2].text))

        data.append(csv_radek)

    return data


def ulozeni_tabulky(csv_file, csv_data):
    with open(csv_file, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for row in csv_data:
            spamwriter.writerow(row)