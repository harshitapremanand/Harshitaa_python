Record = {}
Record = {'id' : 101, 'name' : 'Amit Kumar', 'age' : 21}
del Record['id']
del Record['age']
print(Record)
del Record
print(Record)
Record = {'id' : 101, 'name' : 'Amit Kumar', 'age' : 21}
ele = Record.pop('id')
print('Deleted value is:', ele)
ele = Record.pop('age')
print('Deleted value is:', ele)
Record = {'id' : 101, 'name' : 'Amit Kumar', 'age' : 21}
ele = Record.popitem()
print('Deleted value is:', ele)
ele = Record.popitem()
print('Deleted value is:', ele)