empty_dict ={}
emd = dict(())
print(type(empty_dict))
print(type(emd))

dict1 ={
    'key1':'value1',
    'key2':True,
    'key3':20,
}

print(dict1.get('key11'))

dict1.pop('key1')
print(dict1)

dict1.popitem()
print(dict1)
print(dict1.keys())
print(dict1.values())