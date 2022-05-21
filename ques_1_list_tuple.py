# to create a list of tuples sorted in ascending order by last value of tuple in list
lst1=[]
set_1=int(input("Enter the range of lst1 as:"))
for i in range(1,set_1+1):
    data=int(input("Enter values of lst1 as:"))
    lst1.append(data)
print("lst1 is :",lst1)

lst2=[]
set_2=int(input("Enter the range of lst2 as:"))
for i in range(1,set_2+1):
    data=int(input("Enter values of lst2 as:"))
    lst2.append(data)
print("lst2 is :",lst2)

lst3=list(zip(lst1,lst2))
print("The final list of tuples 'before' sorting is:")
print(lst3)

for i in range(len(lst3)):
    for j in range(i+1,len(lst3)):
        if lst3[i][-1]>lst3[j][-1]:
            temp=lst3[i]
            lst3[i]=lst3[j]
            lst3[j]=temp
print("The final list of tuples 'after' sorting :")
print(lst3)






