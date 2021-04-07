dict1 = {1: 1, 2: 9, 3: 4}
sorted_values = sorted(dict1.values())
print(sorted_values)
 # Sort the values
sorted_dict = {}

for i in sorted_values:
    for k in dict1.keys():
        if dict1[k] == i:
            sorted_dict[k] = dict1[k]
            break

print(sorted_dict)
