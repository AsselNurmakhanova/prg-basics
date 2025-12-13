
def ms_to_kmh(ms):
    return lambda ms : ms * 3.6

result = ms_to_kmh(10)
print(result(10))