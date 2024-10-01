#1
dog={

}
#2
dog['name']='rex'
dog['color']='white'
dog['breed']='german shephered'
dog['legs']=4
dog['age']=3
print(dog)


print("#"*10)
#3
student ={
    'first_name' :"Elvira",
    'last_name':"Moraa",
    'gender':"Female",
    'age':29,
    'marital_status':"Single",
    'Skills':["cooking",'getting angry','swimming'],
    'country' :"Kenya",
    'City':"Nyamira",
    'address':2500
}
#4
print(len(student))
#5
print(type(student.get("Skills")))
#6
student["Skills"].append("Beatiful")
print(student['Skills'])
#7
print(student.keys())
#8
print(student.values())
#9
print(student.items())
#10
del student["Skills"]
print(student)

del student
print(student)