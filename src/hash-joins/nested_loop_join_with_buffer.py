'''
    Nested-Loop Join Algorithm
'''

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

JOIN_BUFFER = []
BUFFER_SIZE = 7


def is_buffer_full():
    'check if we are able to pull data into buffer. Originally checked by memory'
    return len(JOIN_BUFFER) > BUFFER_SIZE


def add_to_buffer(row_table1, row_table2):
    'Push tb1 & tb2 combination to buffer'
    JOIN_BUFFER.append([row_table1, row_table2])


def send_result(result_row1, result_row2, result_row3):
    'send data to client'
    RESULT.append({'id': row1['id'], 'value': row1['value'],
                   'row_table_1': result_row1['table'],
                   'row_table_2': result_row2['table'],
                   'row_table_3': result_row3['table'], })


def compare_with_buffer():
    'Check buffer values and compare with row'
    global OPERATIONS
    global TABLE_READS
    TABLE_READS += 1
    for buffer_row in JOIN_BUFFER:
        for row3 in TABLE3:
            OPERATIONS += 1

            # join conditions here
            if row3['value'] == buffer_row[0]['value']:
                send_result(buffer_row[0], buffer_row[1], row3)


for row1 in TABLE1:
    for row2 in TABLE2:
        add_to_buffer(row1, row2)
        if is_buffer_full():

            compare_with_buffer()
            JOIN_BUFFER = []

compare_with_buffer()

print('count of operations: %s' % OPERATIONS)
print('count of table scan: %s' % TABLE_READS)
