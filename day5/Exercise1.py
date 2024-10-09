#1
myList=[]
Mylist=list(())

#2
counties = ["Nairobi","Nakuru","Mombasa","Kisumu","Vihiga"]

#3
print(len(counties))
#4
print(counties[0], counties[len(counties)//2], counties[-1])
#5
mixed_data_type=["Kelvin",29,5,"single",2500]
name,age,height,marital_status,address=mixed_data_type
#6
it_companies = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
#7
print(it_companies)
#8
print(len(it_companies))
#9
print(it_companies[0], it_companies[len(counties)//2], it_companies[-1])
#10
it_companies[0]="Huwawei"
print(it_companies)
#11
it_companies.append("Cisco")
print(it_companies)
#12
it_companies.insert(len(it_companies)//2,"NAYA")
print(it_companies)
#13
it_companies[0]=it_companies[0].upper()
print(it_companies)
#14
# it_companies="#".join(it_companies)
print(it_companies)
#15
print("NAYA" in it_companies)
#16
it_companies.sort()
print(it_companies)
#17
it_companies.sort(reverse=True)
print(it_companies)

#18
print(it_companies[3:])

#19
# it_companies = it_companies[]
it_companies = it_companies[:len(it_companies) - 3]
print(it_companies)