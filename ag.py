def age():
    print("how old are you:")
    try:
        age= int(input())
        return age
    except ValueError:
        return"that was not a valid input"
print(age())
