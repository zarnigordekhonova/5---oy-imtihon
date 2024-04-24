# 5 - masala
import psycopg2
from prettytable import PrettyTable

def connect():
    database = {
            'dbname': 'python_connect',
            'host': 'localhost',
            'port': 5432,
            'user': 'postgres',
            'password': 'missdezi06'
        }
    conn = psycopg2.connect(**database)
    curr = conn.cursor()

    def select():
        curr.execute(f'SELECT *FROM products')
        table = PrettyTable()
        table.field_names = ([i[0] for i in curr.description])

        table.add_rows(
            curr.fetchall()
        )
        print(table)
        conn.commit()
        conn.close()
    return select()

connect()


