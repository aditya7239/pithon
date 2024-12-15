lst = [12, 35, 9, 56, 24]
n = len(lst)
lst[0], lst[n-1] = lst[n-1], lst[0]
print(lst)
