grades = [37,51,44,23,78,92,39,84,83,51]
res70 = list(filter(lambda x: x > 70, grades))
res40 = list(filter(lambda x: x > 40, grades))
res30 = list(filter(lambda x: x > 30, grades))
print(res70)
print(res40)
print(res30)