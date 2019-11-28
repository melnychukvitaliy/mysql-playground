'''
    Hash Join Algorithm
'''
import hashlib

TABLE1 = [
    {'id': 1, 'value': 'row1', 'table': 't1'},
    {'id': 2, 'value': 'row2', 'table': 't1'},
    {'id': 3, 'value': 'row3', 'table': 't1'},
    {'id': 4, 'value': 'row4', 'table': 't1'},
    {'id': 5, 'value': 'row5', 'table': 't1'},
    {'id': 6, 'value': 'row6', 'table': 't1'},
    {'id': 7, 'value': 'row7', 'table': 't1'},
]


TABLE2 = [
    {'id': 1, 'value': 'row1', 'table': 't2'},
    {'id': 2, 'value': 'row2', 'table': 't2'},
    {'id': 3, 'value': 'row3', 'table': 't2'},
    {'id': 4, 'value': 'row4', 'table': 't2'},
    {'id': 5, 'value': 'row5', 'table': 't2'},
    {'id': 6, 'value': 'row6', 'table': 't2'},
    {'id': 7, 'value': 'row7', 'table': 't2'},
]


TABLE3 = [
    {'id': 1, 'value': 'row1', 'table': 't3'},
    {'id': 2, 'value': 'row2', 'table': 't3'},
    {'id': 3, 'value': 'row3', 'table': 't3'},
    {'id': 4, 'value': 'row4', 'table': 't3'},
    {'id': 5, 'value': 'row5', 'table': 't3'},
    {'id': 6, 'value': 'row6', 'table': 't3'},
    {'id': 7, 'value': 'row7', 'table': 't3'},
]

OPERATIONS = 0
TABLE_READS = 0

RESULT = []


def hash_key(value):
    'Hashing func'
    return hashlib.sha1(value.encode()).hexdigest()


def hash_table(data, column):
    'get table in memory format'
    result = {}
    for row in data:
        result[hash_key(row[column])] = row
    return result


# UPLOAD TO MEMORY
TABLE1_HASHES = hash_table(TABLE1, 'value')
TABLE2_HASHES = hash_table(TABLE2, 'value')
TABLE3_HASHES = hash_table(TABLE3, 'value')

TABLE_READS = 3

OPERATIONS = 0

RESULT = []

for row1 in TABLE1:
    row2 = TABLE2_HASHES[hash_key(row1['value'])]
    row3 = TABLE3_HASHES[hash_key(row1['value'])]

    RESULT.append({'id': row1['id'], 'value': row1['value'],
                   'row_table_1': row1['table'],
                   'row_table_2': row2['table'],
                   'row_table_3': row3['table'], })

    OPERATIONS += 2

print('count of operations: %s' % OPERATIONS)
print('count of table scan: %s' % TABLE_READS)
