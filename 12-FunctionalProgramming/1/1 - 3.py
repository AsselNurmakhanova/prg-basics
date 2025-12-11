
def ms_to_kmh(ms):
    return lambda ms : ms * 3.6

r1 = ms_to_kmh(10)
print(r1(10))
