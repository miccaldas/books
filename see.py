from mysql.connector import connect, Error
from colr import color


def see():
    try:
        conn = connect(
            host="localhost",
            user="mic",
            password="xxxx",
            database="shelves")
        cur = conn.cursor()
        query = """ SELECT * FROM shelves """
        cur.execute(query)
        records = cur.fetchall()
        for row in records:
            print(color(' [*] ID » ', fore='#85a585'), color(str(row[0]), fore='#fdf3d3'))   # 1
            print(color(' [*] BOOKCASE » ', fore='#85a585'), color(str(row[1]), fore='#fdf3d3'))
            print(color(' [*] SHELVE » ', fore='#85a585'), color(str(row[2]), fore='#fdf3d3'))
            print(color(' [*] TITLE ', fore='#85a585'), color(str(row[3]), fore='#f29b85'))
            print(color(' [*] AUTHOR » ', fore='#85a585'), color(str(row[4]), fore='#fdf3d3'))
            print(color(' [*] ISBN » ', fore='#85a585'), color(str(row[5]), fore='#fdf3d3'))
            print(color(' [*] SUMMARY » ', fore='#85a585'), color(str(row[6]), fore='#fdf3d3'))
            print(color(' [*] DATE » ', fore='#85a585'), color(str(row[7]), fore='#fdf3d3'))
            print(color(' [*] NUMBER PAGES » ', fore='#85a585'), color(str(row[8]), fore='#fdf3d3'))
            print('\n')
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if(conn):
            conn.close()


if __name__ == '__main__':
    see()
