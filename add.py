import time
from mysql.connector import connect, Error
from colr import color
import click


def add():
    bookcase = input(color(' Bookcase » ', fore='#f29b85'))
    shelve = input(color(' Shelve » ', fore='#f29b85'))
    title = input(color(' Title » ', fore='#f29b85'))
    author = input(color(' Author » ', fore='#f29b85'))
    isbn = input(color(' ISBN » ', fore='#f29b85'))
    date = input(color(' Year » ', fore='#f29b85'))
    pages = input(color(' Page Number » ', fore='#f29b85'))
    summary = click.edit()
    time.sleep(0.3)

    answers = [bookcase, shelve, title, author, isbn, summary, date, pages]

    try:
        conn = connect(
            host="localhost",
            user="mic",
            password="xxxx",
            database="shelves")
        cur = conn.cursor()
        query = """ INSERT INTO shelves (bookcase, shelve, title, author, isbn, summary, date, pages) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """
        cur.execute(query, answers)
        conn.commit()

    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if(conn):
            conn.close()


if __name__ == '__main__':
    add()
