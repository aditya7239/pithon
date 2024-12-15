Cand = {
    "Amit": {"City": "Delhi", "Age": 23},
    "Sumit": {"City": "Mumbai", "Age": 28},
    "Pooja": {"City": "Delhi", "Age": 32},
    "Kajal": {"City": "Delhi", "Age": 24},
    "Seema": {"City": "Chennai", "Age": 27}
}

candidates = []
for name, details in Cand.items():
    if details["City"] == "Delhi" and details["Age"] < 25:
        candidates.append(name)

print(f"The candidate(s) who live in Delhi and are below 25 years of age are: {candidates}.")
