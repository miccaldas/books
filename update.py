import time
from mysql.connector import connect, Error
import click
from colr import color


def update():
    coluna = input(color(' Column? » ', fore='#f29b85'))
    ident = input(color(' ID? » ', fore='#f29b85'))
    print(color(' Write your update', fore='#f29b85'))
    time.sleep(0.3)
    update = click.edit()

    try:
        conn = connect(
            host="localhost",
            user="mic",
            password="xxxx",
            database="shelves")
        cur = conn.cursor()
        query = "UPDATE shelves SET " + coluna + " = '" + update + "' WHERE id = " + ident
        cur.execute(query,)
        conn.commit()

    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if(conn):
            conn.close()


if __name__ == '__main__':
    update()
