'''
    Nested-Loop Join Algorithm
'''

TABLE1 = [
    {'id': 1, 'value': 'row1', 'table': 't1'},
    {'id': 2, 'value': 'row2', 'table': 't1'},
    {'id': 3, 'value': 'row3', 'table': 't1'},
]


TABLE2 = [
    {'id': 1, 'value': 'row1', 'table': 't2'},
    {'id': 2, 'value': 'row2', 'table': 't2'},
    {'id': 3, 'value': 'row3', 'table': 't2'},
]


TABLE3 = [
    {'id': 1, 'value': 'row1', 'table': 't3'},
    {'id': 2, 'value': 'row2', 'table': 't3'},
    {'id': 3, 'value': 'row3', 'table': 't3'},
]

OPERATIONS = 0

RESULT = []

for row1 in TABLE1:
    for row2 in TABLE2:
        for row3 in TABLE1:
            OPERATIONS = OPERATIONS + 1
            # join conditions here
            if row3['value'] == row1['value']:
                # selected columns
                RESULT.append({'id': row1['id'], 'value': row1['value'],
                               'row_table_1': row1['table'],
                               'row_table_2': row2['table'],
                               'row_table_3': row3['table'], })

print('count of operations: %s' % OPERATIONS)
