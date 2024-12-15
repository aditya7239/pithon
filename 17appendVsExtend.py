lst1 = [1, 2, 3]
lst2 = [4, 5]
lst1.append(lst2)
print("After append:", lst1)  # Output: [1, 2, 3, [4, 5]]

lst1 = [1, 2, 3]
lst1.extend(lst2)
print("After extend:", lst1)  # Output: [1, 2, 3, 4, 5]
