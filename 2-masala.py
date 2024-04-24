import psycopg2

database = {
 'dbname': 'python_connect',
    'host': 'localhost',
    'port': 5432,
    'user': 'postgres',
    'password': 'missdezi06'
}


conn = psycopg2.connect(**database)
curr = conn.cursor()

def create_table(table_name):
    try:
        curr.execute(f'CREATE TABLE {table_name}(id serial PRIMARY KEY, name varchar(64), price numeric, color varchar(32))')
    except Exception as error:
        print(f'Xatolik bor!\n{error}')
    else:
        print('CREATE TABLE')

# create_table('Products')


def insert_into(table_name):
    curr.execute(f'SELECT *FROM {table_name}')
    c_name = ([i[0] for i in curr.description])
    input_data = [input(f'{i} ni kiriting: ') for i in c_name]

    try:
        curr.execute(f'INSERT INTO {table_name} values{tuple(input_data)}')
    except Exception as error:
        print(f'Xatolik bor\n{error}')
    else:
        print('DATA INSERTED')


insert_into('products')


conn.commit()
conn.close()
