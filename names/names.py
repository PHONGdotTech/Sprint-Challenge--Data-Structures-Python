import time
from binary_search_tree import *

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
# Polynomial run time
# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

##############################################################
# # ? run time
# # loop through one list and see if it exists in other list
# for name in names_1:
#     if name in names_2:
#         duplicates.append(name)

# ##############################################################
# logarithmic run time
# create a binary search tree using the first list
bst = BSTNode("name")
for name in names_1:
    bst.insert(name)

# loop through second list, and check if bst contains each name
for name in names_2:
    if bst.contains(name) is True:
        duplicates.append(name)

##############################################################
# # stretch
# for each in set(names_1).intersection(names_2):
#     duplicates.append(each)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
