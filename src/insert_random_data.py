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
MAX_RAND_INT = 1000000
ELEMENTS = 200000


def fill_t1_table():
    'Fill `t1` table with random items'
    cursor = DB.cursor()
    current_item = 0
    for _ in range(ELEMENTS):
        cursor.execute(
            'INSERT INTO t1 (c1, c2) VALUES (%s, %s)',
            randint(0, MAX_RAND_INT), randint(0, MAX_RAND_INT))

        DB.commit()
        current_item = current_item + 1
        if current_item % 1000 == 0:
            print(current_item, "records inserted.")


def fill_t2_table():
    'INSERT the same items into `t2` item'
    cursor = DB.cursor()
    cursor.execute(
        'INSERT INTO t2 (c1, c2) SELECT c1, c2 FROM t1',
        randint(0, MAX_RAND_INT), randint(0, MAX_RAND_INT))


fill_t1_table()
fill_t2_table()
