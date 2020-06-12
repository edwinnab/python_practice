subject = {"maths": 34, "English": 67, "kiswahili": 65, "science": 78}
subject["cre"] = 34#add key_pair value
subject["cre"] = 78#modify
del subject["cre"]#deletes key-value pair
for units in subject:#iterate over keys
    print(units)
for num in subject.values():#iterate over values
    print(num)
for units in subject.items():#iterate over key_value pair
    print(units)
for key, value in subject.items():#iterate over key with coresponding key,value with coresponding value
    print("key:", key, "; value:", value)
print("maths" in subject)#checks key in dictionary
print(78 in subject.values())#checks value in dictionary.
print(len(subject))#length of dictionary
print(subject)