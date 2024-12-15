R = {"OM": 76, "JAI": 45, "BOB": 89, "ALI": 65, "ANU": 90, "TOM": 82}
name_list = []
for name, marks in R.items():
    if marks > 75:
        name_list.append(name)
print("The names of the students with marks greater than 75 in reverse order are:")
for name in reversed(name_list):
    print(f"{name}", end=" ")
