arr = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
longest_name = arr[0]
i = 1
while i < len(arr):
    if len(arr[i]) > len(longest_name):
        longest_name = arr[i]
    i += 1
print("Longest name:", longest_name)