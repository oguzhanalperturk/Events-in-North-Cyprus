import sqlite3


def createDatabase(dbname):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    c.execute("CREATE TABLE city("
              "cityid INTEGER PRIMARY KEY,"
              "cityname TEXT)")

    c.execute("CREATE TABLE event("
              "eventid INTEGER PRIMARY KEY AUTOINCREMENT,"
              "name TEXT,"
              "description TEXT,"
              "price INTEGER,"
              "date TEXT,"
              "time TEXT,"
              "location TEXT,"
              "isActive INTEGER,"
              "event_city_id INTEGER,"
              "event_username TEXT,"
              "FOREIGN KEY (event_city_id) REFERENCES city(cityid),"
              "FOREIGN KEY (event_username) REFERENCES user(username))")

    c.execute("CREATE TABLE user("
              "username TEXT PRIMARY KEY,"
              "password TEXT,"
              "firstname TEXT,"
              "lastname TEXT,"
              "email TEXT)")

    conn.commit()


def insertCity(dbname):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    c.execute("INSERT INTO city VALUES(?,?)", (1, "Lefkosa"))
    c.execute("INSERT INTO city VALUES(?,?)", (2, "Girne"))
    c.execute("INSERT INTO city VALUES(?,?)", (3, "Guzelyurt"))
    c.execute("INSERT INTO city VALUES(?,?)", (4, "Gazi Magusa"))
    c.execute("INSERT INTO city VALUES(?,?)", (5, "Lefke"))
    c.execute("INSERT INTO city VALUES(?,?)", (6, "Iskele"))

    conn.commit()


if __name__ == "__main__":
    createDatabase("database.db")
    insertCity("database.db")
