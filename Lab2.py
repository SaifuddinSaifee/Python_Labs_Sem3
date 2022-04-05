# # LAB 2 : 

num1 = int(input("Enter the number of elements in list 1 :"))
list1 = []
printf ("Enter the elements you want in list 1: ")
for i in range()

list2 = []


# ## Method 1 : using + operator

print("Method 1 : using + operator")
joined_list1 = list1 + list2
print("Concatenation of list1 : {} and list2 : {} is {}\n" .format(list1,list2,joined_list1))


# ## Method 2 : Using * operator

print("Method 2 : Using * operator")
joined_list2 = [*list1, *list2]
print("Concatenation of list1 : {} and list2 : {} is {}\n" .format(list1,list2,joined_list2))


# ## Method 3 : Using extend() function

print("Method 3 : Using extend() function")
joined_list3 = list2.extend(list1)
print("Concatenation of list1 : {} and list2 : {} is {}\n" .format(list1,list2,joined_list3))


# ## Method 4 : Using itertools.chain

print("Method 4 : Using itertools.chain")
import itertools
joined_list4 = list(itertools.chain(list1, list2))
print("Concatenation of list1 : {} and list2 : {} is {}\n" .format(list1,list2,joined_list4))


# ## Method 5 : using append function

print("Method 5 : using append function")
for value in list2:
    list1.append(value)
print("Concatenation of list1 : {} and list2 : {} is {}\n" .format(list1,list2, list2))


# ## UNION of two list
 
 joined_list5 = list(set(list1+list2))
 print("Union of list 1 and list 2 =", joined_list5)

