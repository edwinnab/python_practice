num_3 = [1,2,4,6,7,8,] 
num_5 = [5,10,15]
for i in range(1,101):
    if i in num_3:
        print("Fizz")
    elif i in num_5:
        print("Buzz")
    else:
        continue
    print(i)
