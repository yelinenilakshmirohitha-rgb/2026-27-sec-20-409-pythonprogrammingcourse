dict1 = {"name": "Rahul", "age": 18}
dict2 = {"course": "Python", "city": "Delhi"}

merged_dict = dict1.copy()   # Copy dict1, so the original is not changed
merged_dict.update(dict2)

print("Original dict1:", dict1)
print("Original dict2:", dict2)
print("Merged dictionary:", merged_dict)