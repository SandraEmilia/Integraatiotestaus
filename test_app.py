import os
import tempfile
import pytest
import app

@pytest.fixture  #Fixture on pytest-kirjaston mekanismi, joka määrittelee testifunktion valmistelun ja puhdistuksen ennen ja jälkeen testin suorittamista. 

def test_db(monkeypatch):    #Luodaan väliaikainen tietokanta testausta varten. Monkeypatch -objekti mahdollistaa tiettyjen asioiden korvaamisen testauksen ajaksi.
    temp_db = tempfile.NamedTemporaryFile(delete=False)      # Luo tilapäisen tiedoston tietokannalle
    monkeypatch.setattr(app, "DB_NAME", temp_db.name)       # Korvataan sovelluksen DB_NAME väliaikaisella tiedostopolulla
    app.init_db()
    yield     # Testi suoritetaan tässä vaiheessa (yield on osa pytest-fixturea)
    temp_db.close()
    os.unlink(temp_db.name)         #Poistaa väliaikaisen tietokannan

def test_add_and_get_users():    #Luodaan funktio, jonka avulla testataan käyttäjän lisäämistä ja hakemista tietokannasta
    app.add_user("Maija")        #Lisätään käyttäjä nimeltä Maija
    users = app.get_users()      #Haetaan käyttäjät tietokannasta
    assert len(users) == 1       #Varmistetaan, että käyttäjiä on yksi
    assert users[0][1] == "Maija"   #Varmistetaan, että käyttäjän nimi on Maija
