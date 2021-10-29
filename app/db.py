import sqlite3
from sqlite3 import Error

def get_db():
    try:
        con = sqlite3.connect('cuatro.db')
        return con
    except Error:
        print(Error)


def insert_datos(usuario, correo, contrasena):
    strsql = "INSERT INTO usuario2021(usuario, correo, contrasena) VALUES('"+usuario+"','"+correo+"', "+contrasena+");"
    con = get_db()
    cursorObj = con.cursor()
    cursorObj.execute(strsql)
    con.commit()
    con.close()



