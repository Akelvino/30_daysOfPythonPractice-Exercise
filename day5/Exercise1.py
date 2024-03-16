list =[]
country =['kenya','uganda','tanzania','somalia','haiti']

print(len(country))

print(country[0], country[2], country[-1])

mixed_data_types =['kelvin',28, 6.5, False, {'regio':'kitengela','address':'2500'}]

it_companies =['Facebook','Google','microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0],it_companies[len(it_companies)//2],it_companies[-1])
it_companies.pop()
print(it_companies)
it_companies.append('PLP')
print(it_companies)
it_companies.insert(2,'CodeAfrica')
print(it_companies)

it_companies[3]=it_companies[3].upper()
print(it_companies)

# it_companies='#'.join(it_companies)
# print(it_companies)

print("Apple" in it_companies)

it_companies =it_companies[2:]
print(it_companies)

it_companies = it_companies[:len(it_companies)-3]
print(it_companies)

it_companies.pop(0)
print(it_companies)

del it_companies
# print(it_companies)

front_end = ['HTML','CSS','JS','React','Redux']
back_end = ['Node','Express','MongoDB']

front_end.extend(back_end)
print(front_end)

full_stack = front_end
print(full_stack)

# full_stack.append("SQL")
print(full_stack + ['Python','SQL'])