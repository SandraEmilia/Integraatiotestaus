import sqlite3  #Käytetään Pythonin sisäänrakennettua SQLlite -kirjastoa, jonka avulla voidaan käyttää SQL-tietokantaa sovelluksessa.

DB_NAME = "users.db" #Määritetään tietokannan tiedostonimi

def init_db():     #Luodaan funktio, joka alustaa tietokannan, jos sitä ei ole vielä olemassa
    connection = sqlite3.connect(DB_NAME)    #Yhdistetään tietokantaan
    cursor = connection.cursor()    #Luodaan kursori, jolla voidaan suorittaa SQL-komentoja
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")    #Luodaan uusi taulu, jos sitä ei ole jo olemassa
    connection.commit()    #Tallentaa muutokset tietokantaan
    connection.close()    #Sulkee tietokannan

def add_user(name):    #Luodaan funktio, jolla voidaan lisätä käyttäjiä tietokantaan
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))  #Lisää käyttäjän users -tauluun
    connection.commit()
    connection.close()

def get_users():    #Luodaan funktio, joka palauttaa käyttäjät tietokannasta
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()     #Haetaan kaikki käyttäjät
    connection.close()
    return users




