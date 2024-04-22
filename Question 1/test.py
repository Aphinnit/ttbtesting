# Check duplicate items from list A and list B and append to a new list. Using your
# preferred programming language.
# List A : [1,2,3,5,6,8,9]
# List B : [3,2,1,5,6,0]

list_A = [1, 2, 3, 5, 6, 8, 9]
list_B = [3, 2, 1, 5, 6, 0]

duplicate_items = list(set(list_A) & set(list_B))

# new list
new_list = []
for item in duplicate_items:
    new_list.append(item)

print("Items from list A and list B:", new_list)
 