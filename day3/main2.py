print(len("python") is not len("dragon"))

print("on" in "python" and "on" in "jargon")

print("jargon" in "I hope this course in not full of jargon")

x=(float(len("python")))
x=str(x)
print(type(x))

#calculating payment 
hoursWorked = int(input("Enter hours: "))
ratePerhour = int(input("Enter rate per hour: "))
print("Your weekly earning is {}".format(hoursWorked*ratePerhour))
