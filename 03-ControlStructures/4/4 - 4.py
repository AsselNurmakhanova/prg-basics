university = 'Krakow University of Economics'
university_expanded = ''

for char in university:
    university_expanded = university_expanded + char + ' '
university_expanded = university_expanded.strip()
# Print both the original and the expanded names
print(university)          # original university name
print(university_expanded) # expanded university name