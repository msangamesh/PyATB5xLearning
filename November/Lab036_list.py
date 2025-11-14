
my_list = [1,2,3,4,5]
my_list2 = ["ravi",7,8,"ram",10,20]

print(my_list)
print(type(my_list))
print(len(my_list))
print(len(my_list2))
print(my_list2[3])
print(my_list[4])

my_list.append(6)
print(my_list)
my_list2.extend(my_list)
print(my_list2)
my_list2.remove("ram")
print(my_list2)
my_list2.reverse()
print(my_list2)
my_list2.remove("ravi")
print(my_list2)
my_list2.sort()
print(my_list2)
my_list2.sort(reverse=True)
print(my_list2)

