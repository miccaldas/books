from mysql.connector import connect, Error
from colr import color


def search():
    try:
        busca = input(color(' What are you searching for? ', fore='#f29b85'))
        conn = connect(
            host="localhost",
            user="mic",
            password="xxxx",
            database="shelves")
        cur = conn.cursor()
        query = " SELECT * FROM shelves WHERE MATCH(bookcase, shelve, title, author, summary) AGAINST ('" + busca + "' IN NATURAL LANGUAGE MODE)"
        cur.execute(query)
        records = cur.fetchall()
        for row in records:
            print(color(' [*] ID » ', fore='#85a585'), color(str(row[0]), fore='fdf3d3'))
            print(color(' [*] BOOKCASE » ', fore='#85a585'), color(str(row[1]), fore='#fdf3d3'))
            print(color(' [*] SHELVE » ', fore='#85a585'), color(str(row[2]), fore='#fdf3d3'))
            print(color(' [*] TITLE ? ', fore='#85a585'), color(str(row[3]), fore='#fdf3d3'))
            print(color(' [*] AUTHOR » ', fore='#85a585'), color(str(row[4]), fore='#fdf3d3'))
            print(color(' [*] ISBN » ', fore='#85a585'), color(str(row[5]), fore='#fdf3d3'))
            print(color(' [*] SUMMARY » ', fore='#85a585'), color(str(row[6]), fore='#fdf3d3'))
            print(color(' [*] DATE » ', fore='#851585'), color(str(row[7]), fore='#fdf3d3'))
            print(color(' [*] PAGE NUMBER » ', fore='#85a585'), color(str(row[8]), fore='#fdf3d3'))
            print('\n')
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if(conn):
            conn.close()


if __name__ == '__main__':
    search()
