
my_list =[1,2,3,4,5]
print(my_list,end='')
print(len(my_list))

# append()
my_list.append(6)
my_list.append(7)
print(my_list,end='')
print(len(my_list))

# extend()
my_list.extend([9,10,11])
print(my_list,end='')
print(len(my_list))

#  insert

my_list.insert(2,"Sangu")
print(my_list,end='')
print(len(my_list))

# Results
# [1, 2, 3, 4, 5]5
# [1, 2, 3, 4, 5, 6, 7]7
# [1, 2, 3, 4, 5, 6, 7, 9, 10, 11]10
# [1, 2, 'Sangu', 3, 4, 5, 6, 7, 9, 10, 11]11

#  Remove
my_list.remove(3)
print(my_list,end='')
print(len(my_list))


# copy
my_copy_list = list(my_list)
print("---")
print(my_copy_list,end='')
print(len(my_copy_list))

my_copy_list = my_list.copy()
print("---")
print(my_copy_list,end='')
print(len(my_copy_list))

# sort

my_copy_list.remove("Sangu")
print(my_copy_list,end='')
print(len(my_copy_list))

my_copy_list.insert(7,15)
print(my_copy_list,end='')
print(len(my_copy_list))

my_copy_list.sort()
print(my_list,end='')
print(my_copy_list,end='')


