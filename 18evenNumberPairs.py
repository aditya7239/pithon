pairs = [(2, 5), (4, 2), (9, 8), (12, 8)]
count = sum(1 for a, b in pairs if a % 2 == 0 and b % 2 == 0)
print("Number of pairs with both elements even:", count)
