# domain-ja-ip-parit-shodanista

Myönnetään, ei mikään seksikkäin nimi, mutta nimi kummiskin. Tämä on pikaisesti kyhätty ohjelma (yksittäinen funktio), jolla saadaan haettua shodanista domain ja ip-osoite pari yhdellä hakulausekkeella. 

Käyttötarkoitus tälle ohjelmalle oli domainien oikeiden IP-osoitteiden selvittäminen. On tilanteita, joissa Cloudflare tarjoaa web scrapeamiselta tai boteilta suojan, mutta shodanista löytää oikean ip-osoitteen tietyillä hakusanoilla. 

## Esimerkkikäyttö

Kopioi `shodan_search.py` omaan projektiisi. Tiedostossa `esimerkki.py` on esimerkki ohjelman/funktion käytöstä omassa python-projektissa. Muista lisätä [requirements.txt](requirements.txt)-tiedoston sisältö omaan `requirements.txt`-tiedostoosi.

Ohjelma palauttaa JSON-muodossa datan. Esimerkki:

```JSON
{
    "amount": 696, 
    "results": [
        {"ip": "1.1.1.1", "domain": "cloudflare.com"}, 
        {"ip": "8.8.8.8", "domain": "google.com"}
    ], 
    "error": ""
}

```