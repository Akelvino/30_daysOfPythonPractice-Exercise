#list
#it is a collection of data type which are mutable, ordered, indexed and has different data type

#creating a list using the built in function 

lst =list() #using built in function
# lst =[]#using squre bracket

fruits = ['banana','orange','mango','lemon']
vegetables= ['Tomato','potato','cabbage','onion']
web_tech = ['HTML','CSS','JS','React']
print(fruits)
print(len(web_tech))

#list can have different data types

mrMe =['kelvin',29,False,{'country':"kenya","children":'none'}]
print(mrMe[::-1])

#unpacking
a,b,*rest = mrMe
print(rest)

#slicing
print(web_tech[1:3])

#modifying
web_tech[0]="Software Engineering"
print(web_tech)

print("CSS" in web_tech)

lst.append("Emily")
print(lst)

lst.insert(1,'Joan')
print(lst)
lst.insert(1,'Emily')
print(lst)
lst.remove('Joan')
print(lst)

#pop is used to delete a specific index 
#del is used to delete items within an index or the entire list

print(lst.pop())

print(fruits)

print(fruits[::-1])
print(sorted(fruits))