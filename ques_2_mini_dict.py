# create your own mini dictionary where keys are a-z and values are corresponding ASCII values
lst_keys=[]
set=int(input("Enter the range of lst_keys:"))
for i in range(1,set+1):
    data=input("Enter your keys:")
    lst_keys.append(data)
print("The list of keys is given as: ")
print(lst_keys)

lst_values=[]
for i in range(97,123,1):
    lst_values.append(i)
print("The list of ASCII values is given as :")
print(lst_values)

output=dict(zip(lst_keys,lst_values))
print("The dictionary with keys as 'a_z' and values as 'ASCII' values is given by:")

print(output)
