 #List-- collection of items
 # Duplicates are allowed in list
 # multiple different data types are allowed
 # stored with index
 # ex my_list=[1,2,3]

my_list = [1,2,3]
my_list2 =[1,"reddy",'true',12.3,"Sanga"]

print(my_list)
print(my_list2)
print(my_list[2])
print(my_list2[1])
print(len(my_list2))

my_list2[0] ="Kishtu"
print(my_list2)

for i in my_list2:
    if i == "true":
      print("Testing done")

