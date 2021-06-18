from mysql.connector import connect, Error
from colr import color


def delete():
    ident = input(color(' ID to delete? » ', fore='#f29b85'))

    try:
        conn = connect(
            host="localhost",
            user="mic",
            password="xxxx",
            database="shelves")
        cur = conn.cursor()
        query = " DELETE FROM shelves WHERE id = " + ident
        cur.execute(query)
        conn.commit()

    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if(conn):
            conn.close()


if __name__ == '__main__':
    delete()
