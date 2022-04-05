# LAB 3 : Program to find intersection of two lists

# **Program logic**
# 1. Write a funtion to find the intersection of two list
# 2. take the input of two lists
# 3. Print the two list
# 4. call the function by passing the two list
# 5. Print the intersection of two list

# ## Define the fuction for finding the intersection of two list

def intersection_list(list1, list2):
    list3 = []
    list3 = [value for value in list1 if value in list2]
    return list3


# ## Initialize two lists

l1 = [1,2,3,4,5,6]
l2 = [4,5,6,7,8,9]


# ## Calling the function
l3 = []
l3 = intersection_list(l1,l2)
print("Intersection of l1 : {} and l2 : {} is l3 : {}".format(l1,l2,l3))

