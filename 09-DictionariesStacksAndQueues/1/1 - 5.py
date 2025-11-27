countries = [
    {"name":"Poland", "population":38000000},
    {"name": "China", "population": 21344556785432},
    {"name": "Luxembourg", "population": 1.5},
    {"name": "Nigeria", "population": 2452523},
    {"name": "Hungary", "population": 13732723}
]
print(f"{'COUNTRY'} {'POPULATION'}")
for country in countries:
    print(f"{country['name']} {country['population']}")