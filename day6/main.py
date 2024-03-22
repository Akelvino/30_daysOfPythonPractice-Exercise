#tuples

empty_tuple = ()
empty_tuple = tuple()

tp1 = ('item1','item2','item3')

fruits =('banana','orange','mango','lemom')

#tpl length
print(len(fruits))

print(fruits[0])
last_index= len(fruits) -1
print(fruits[last_index])

# fruits=fruits[-3:-1]
print(fruits)
fruits= list(fruits)
print(fruits)
fruits.append("carrots")
print(fruits)
fruits=tuple(fruits)
print(fruits)
cerials = ("beans",'soya','green grams')

vegez = fruits+cerials
print(vegez)

#exercise

empty_tpl = ()
sisters =("lucy",'Mary','Emily')
brothers = ('John','peter','erick')

siblings = sisters + brothers
print(siblings)
print(len(siblings))
family = list(siblings)
parents=["joash","babygirl"]
family.extend(parents)
print(family)

siblings = (family[0:6])
print(siblings)

frts =('lemon','orange','mangoe')
vegetables = ('spinach','cabbage','kales','kunde')
animal_product=('milk','skin','meat')

food_stuff_tp = frts+vegetables+animal_product
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
print(len(food_stuff_lt)/2)
food_stuff_lt.pop(5)
print(food_stuff_lt)
food_stuff_lt.remove(0,2)
print(food_stuff_lt)

del food_stuff_tp
print(food_stuff_tp)