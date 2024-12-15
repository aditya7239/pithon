def search_element(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            position = i + 1
            index = i
            return position, index
    return None, None

# Example usage
if __name__ == "__main__":
    my_array = [10, 20, 30, 40, 50]
    search_element_value = 30
    position, index = search_element(my_array, search_element_value)
    
    if position is not None:
        print(f"Array = {my_array}")
        print(f"Search Array Element = {search_element_value}")
        print(f"Element is Found in the Position = {position}")
        print(f"Element is Found in the Index = {index}")
    else:
        print(f"Element {search_element_value} not found in the array.")
