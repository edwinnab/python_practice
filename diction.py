ages = {"gladys": 36, "evans": 34, "edwinna": 25, "john": 16}
print(ages["gladys"])#access value corresponding with the key
ages["talina"] = 35#add a key_value pair
print(ages)
ages["gladys"] = 45 #modify a value corresponding to the key 
del ages["talina"]# deletes a key_value pair
print("gladys" in ages)#checks if key is in dict
print(36 in ages.values())#checks if a value is in dict
print(len(ages))#length of the dict
#iterate over keys
for members in ages:
    print(members)
    #iterate over key_pair values using tuple method .items()
for members in ages.items():
    print(members)
    #iterate over key_value pair using tuple assignment
    #key to assign key and value to assign value
for key, value in ages.items():
    print("key:", key, "; value:", value)
    #iterate over values
for num in ages.values():
    print(num)