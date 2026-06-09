countries = {
    "Italy": "Rome",
    "Kenya": "Nairobi",
    "Germany": "Berlin",
    "France": "Paris",
    "USA": "Washington, D.C",
    "Nigeria": "Abuja",
    "India": "New Delhi",
    "Brazil": "Brasília",
    "UAE": "Abu Dhabi",
    "Singapore": "Singapore",
}
countries.update({"United": "London"})

country = input("Enter the country name: ")

country = country.strip().title() if country.upper() != "USA" else "USA"


if country in countries:
    print(f"The Capital City of {country} is: {countries[country]}.")

else:
    print("No capital for that found")

values = countries.values()
keys = countries.keys()
for key in keys:
    print(key)
    
for value in values:
    print(value)
    



items = countries.items()
for key, value in items:
    print(f"{key}: {value}")

print(countries.get("USA"))