name_list2 = [
    {'id':1, 'name':'田中'},
    {'id':2, 'name':'山田'},
    {'id':3, 'name':'吉田'},
    {'id':4, 'name':'加藤'},
    {'id':5, 'name':'斎藤'}
]

name_list = [
    '田中',
    '山田',
    '吉田',
    '加藤',
    '斎藤',
    '片桐',
]

list = [
    '片桐',
    '山田',
    '加藤',
    '斎藤',
    '田中',
    '吉田',
    '田中',
]

for name in list:
    print(name)

sorted_list = []

for name in name_list:
    if name in list:
        sorted_list.append(name)
    else:
        sorted_list.append(name)

    
print('-----')

for name in sorted_list:
    print(name)