Tämä on integraatiotestausta varten luotu hyvin yksinkertainen sovellus, jossa testataan kahden komponentin (python -pohjainen sovellus ja SQLlite-tietokanta) välistä integraatiota.

Sovelluksessa käytetään Pythonin sisäistä SQLlite -kirjastoa, jonka avulla luodaan yksinkertainen tietokanta ja sinne taulu "users".
Sovellus sisältää funktiot, joiden avulla tauluun voidaan lisätä käyttäjiä  ja sieltä voidaan hakea kaikki käyttäjät. 

Testaus suoritetaan Pytest:llä, joka on Pythonin testauskehys. Pytest etsii automaattisesti kaikki testitiedostot ja -funktiot, joiden nimet alkavat "test_" sanalla. 
Testausta varten on luotu erillinen "test_app.py" -tiedosto. 

Sovellusta testataksesi huolehdi, että asennettuna on:

- Python (https://www.python.org/downloads/)
- Pytest (pip install pytest)

Voit kloonata tämän repositoryn Githubista komennolla:

git clone https://github.com/SandraEmilia/Integraatiotestaus.git

aja testaukset komennolla:

pytest
TAI
python -m pytest (esim. windows)

Testifunktiossa test_add_and_get_users Tietokantaan lisätään käyttäjä "Maija", haetaan kaikki käyttäjät tietokannasta ja varmistetaan, että käyttäjien määrä on 1 ja lisätty käyttäjä on nimeltään "Maija".
Kyseisellä koodilla testin tulee mennä läpi onnistuneesti, joka tarkoittaa sitä, että sovellus toimi odotetulla tavalla ja tietokannan sekä sovelluksen välinen integraatio toimii. 

Jos haluat kokeilla testin epäonnistumista, voit muuttaa esimerkiksi käyttäjien määrää kahteen ja ajaa testin uudelleen:
assert len(users) == 2 
