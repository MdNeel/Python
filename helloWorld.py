print("Practicing List Methods")
list1=[13,8,25,15,7,27]
count=0
list=[]
list.append(8)
list.append(1)
list.append(15)
list.append(55)
list.append(45)
list.append(5)
#for list in list:
    #print(list)

for i in list1:
    count=count+1

print("Items in the list1 are :",list1)   
print("Number of the items in the list1 are :", count)
print("Items in the list are :",list)
list.sort()
print("List after sorting is :",list)
list.pop()
print("List after poping is :",list)
