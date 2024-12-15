city = input("Enter the city name: ").lower()
monuments = {
    'delhi': 'Red Fort',
    'agra': 'Taj Mahal',
    'jaipur': 'Jal Mahal'
}
if city in monuments:
    print(f"The monument of {city.capitalize()} is {monuments[city]}.")
else:
    print("Monument information not available for this city.")
