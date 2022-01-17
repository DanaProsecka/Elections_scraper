# Elections_scraper



## Popis projektu
Tento projekt slouží k extrahování výsledků parlamentních voleb z roku 2017. Odkaz k prohlédnutí pro Jihomoravský kraj [zde](https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6201)

## Instalace knihoven
Pro instalaci doporučuji použít nové virtuální prostředí a program spustit následovně: 

```
pip3 --version
pip3 install -r requirements.txt
```

## Spuštění projektu

Spuštění souboru elections_scraper.py v příkazovém řádku vyžaduje 2 argumenty. 
```
python elections_scraper <odkaz_uzemniho_celku> <vysledny_soubor>
```
Funkční příklad
```
python3 elections_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6201" "vysledek.csv"
```
Výsledky se vám stáhnout do souboru .csv


## Ukázka projektu

Výsledky hlasování pro okres Blansko:

1.argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6201

2.argument: vysledek.csv

Spuštění: 
```
python3 elections_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6201" "vysledek.csv"
```
Očekávaný výsledek: 
```
code,location,registered,envelopes,valid,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů,Národ Sobě
581291,Adamov,3 668,2 157,2 138,208,3,5,222,0,76,241,37,18,28,1,7,208,5,63,565,5,14,117,2,10,3,6,278,15,1
581313,Bedřichov,205,155,153,16,0,2,10,0,3,4,0,3,8,0,0,13,0,6,51,0,1,17,0,0,1,0,18,0,0
```
