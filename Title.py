Cand = {
    "C001": {"Fname": "Pooja", "Lname": "Sharma", "Gen": "F"},
    "C002": {"Fname": "Pankaj", "Lname": "Sahu", "Gen": "M"},
    "C003": {"Fname": "Neha", "Lname": "Roy", "Gen": "F"},
    "C004": {"Fname": "Vivek", "Lname": "Singh", "Gen": "M"}
}

for key, value in Cand.items():
    if value["Gen"] == "F":
        print(f"{key} Ms. {value['Fname']} {value['Lname']}")
    else:
        print(f"{key} Mr. {value['Fname']} {value['Lname']}")
