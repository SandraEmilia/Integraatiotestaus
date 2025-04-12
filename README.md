Tämä on integraatiotestausta varten luotu hyvin yksinkertainen sovellus, jossa testataan kahden komponentin (python -pohjainen sovellus ja SQLlite-tietokanta) välistä integraatiota.

Sovelluksessa käytetään Pythonin sisäistä SQLlite -kirjastoa, jonka avulla luodaan yksinkertainen tietokanta ja sinne taulu "users".
Sovellus sisältää funktiot, joiden avulla tauluun voidaan lisätä käyttäjiä  ja sieltä voidaan hakea kaikki käyttäjät. 

Testaus suoritetaan Pytest:llä, joka on Pythonin testauskehys. Pytest etsii automaattisesti kaikki testitiedostot ja -funktiot, joiden nimet alkavat "test_" sanalla. 
Testausta varten on luotu erillinen "test_app.py" -tiedosto. 
