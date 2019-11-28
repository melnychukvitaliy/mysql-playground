'''
Insert random data into mysql table
'''
from random import randint
import mysql.connector


DB = mysql.connector.connect(
    host="db",
    user="root",
    passwd="123root123",
    database="playground",
    auth_plugin='mysql_native_password'
)
MAX_RAND_INT = 1000
ELEMENTS = 200000


def fill_table_with_random_values(table):
    'Fill `t1` table with random items'
    print('Inserting rows into %s' % table)
    cursor = DB.cursor()
    current_item = 0
    values = []
    sql = 'INSERT INTO %s (c1, c2) %s' % (table, 'VALUES (%s, %s)')
    for _ in range(ELEMENTS):
        values.append((randint(0, MAX_RAND_INT), randint(0, MAX_RAND_INT)),)

        current_item = current_item + 1
        if current_item % 1000 == 0:
            cursor.executemany(sql, values)
            DB.commit()
            values = []
            print(current_item, "records inserted.")


def copy_items(from_table, to_table):
    'INSERT the same items into `t2` item'
    cursor = DB.cursor()
    cursor.execute(
        'INSERT INTO %s (c1, c2) SELECT c1, c2 FROM %s' % (to_table, from_table))
    DB.commit()


fill_table_with_random_values('t1')
fill_table_with_random_values('t2')
copy_items('t1', 't1_idx')
copy_items('t2', 't2_idx')
