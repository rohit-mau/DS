from array import *

my_array = array('i', [10,20,30,40,50])

print("Traversing the array...")
for x in my_array:
 print(x)

print("Accessing array element...")
print (my_array[0])
print (my_array[2])

print("Inserting element in array...")
my_array.insert(1,60)
for x in my_array:
 print(x)

print("Deleting element in array...")
my_array.remove(40)
for x in my_array:
 print(x)

print("Searching index of an element...")
my_array = array('i', [10,20,30,40,50])
print (my_array.index(40))

print("sorting an array...")
array= [40,30,20,10,]
array.sort()
print(array)

print("Merging an array")
list1= ["1","2","3"]
list2 =["4","5","6"]
for x in list2:
	list1.append(x)
print(list1)

print("REVERSING AN ARRAY")
array= [40,30,20,10,]
array.reverse()
print(array)




print("Update an element in array...")
my_array[2] = 80
for x in my_array:
 print(x)
