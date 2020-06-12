"""
def rev(s):
    return s[:: -1]
def pali(s):

    a = rev(s)
    if (s==a):
        return True
    return False
s = input("Enter a string:")
s = rev(s)
print("reverse of string:",s)
s = pali(s)
print("palindrome:",s)
"""

"""
#dictionary
days = {"monday": 12, "Tuesday": 13, "wenesday": 34, "thursday": 67}
#add key_value pair
days["Friday"] = 34
#modify key_value pair
days["Friday"] = 67
#check length
print(len(days))
#deletes 
del days ["Friday"]
#iterate over keys
for elements in days:
    print(elements)
    #check keys
print("monday" in days)
#check values
print(67 in days.values())
#iterate over values
for num in days.values():
    print(num)
    #iterate key_values
for elements in days.items():
    print(elements)
#iterate key and value
for key,value in days.items():
    print("key:", key, ";value:", value)
print(days)
"""
""""
#variables
apples = 23
print(apples)
"""
"""
#control flow if ,elif,else
apples = eval(input("Enter number of apples"))
if apples == 14:
    print("harvest")
elif apples > 14:
    print("harvest and sell")
else:
    print("wait till ready")
"""
"""
  #list
my_integers = [1,2,3,4,4,4,4,]
#index starts from 0
print(my_integers[5])
#list of strings
relatives = ["mum", "dad", "bro", "grandma"]
#add an element
relatives.append("lynn")
print(relatives)
"""
"""
#dict exercises
dict = {"ten": 10, "twenty": 20, "thirty": 30}
dict1 = {"thirty": 30, "fourty": 40, "fifty": 50}
"""
"""
for element in dict.items():
    print(element)
"""
"""
del dict["twenty"]
print(10 in dict.values())
dict["tennn"] = dict.pop("ten")
print(dict)
"""
"""
#checks type
apples = 23
print(type(apples))
relatives = "mother"
print(type(relatives))
dare = True
print(type(dare))
num = 32.36
print(type(num))
num1 = 32
print(type(num1))
name1 = "john"
name2 = "omwando"
ans = name1 + name2
print(ans)
#length of string
print(len(ans))
#replaces part of a string
print(ans.replace("john","edwinna"))
#characters to uppercase
print(ans.upper())
#charcters to lowercase
print(ans.lower())
print(type(ans))
"""
"""
#type casting
#string to int
apples = int("43")
print(apples)
#int to string
apples = str(32)
print(apples)
#int to float
apples = float(36)
print(apples)
#float to int
apples = int(34.45)
print(apples)
#float to str
apples = str(45.00)
print(apples)
#implicit conversion
apples = 32
mango = 45.9
sum = (apples + mango)
print(sum)
#explicit conversion
apples = input("enter number")
mango = 5
sum1 = (int(apples) + mango)
print(sum1)
"""
"""
#floor division
div = 9//2
print(div)
#modulus
div1 = 9%2
print(div1)
#division
div2 = 9/2
print(div2)
#concatination btwn strings and other types
age = "i have" + str(27) + "years"
print(age)
#addition and assignment
x =3
x += 2
print(x)
"""
"""
#list
ages = [1,2,3,4,5,6]
#adds element 
ages.append(8)
#insert element to a specific position
ages.insert(0,"Edwinna")
ages[0] =("John")
#delete specfic element and clear() for the entire list
ages.remove('John')
#checks element in a list
print(1 in ages)
print(ages)
"""
"""
#tuple to update convert to list then to tuple
names = ("john","edwinna","sarah")
nam = list(names)
nam[2] = "sam"
names = tuple(nam)
print(names)
street = ("shaabab", "rhondaa", "kanu")
streets = list(street)
streets[0] = "upendo"
street = tuple(streets)
print(street)
#reference element
print(street[2])
print("shaabab" not in street)
"""
"""
#set
names = {"john", "kelly", "keziah", "samuel", "sarah"}
#add a single element
names.add("mary")
#add multiple elements
names.update(["zippy", "linety", "omwando", "happiness"])
#remove() to delete specific element
names.remove("mary")
#clear()for the entire set
print(names)
"""
"""
#dict
doors = {"one": 1, "two": 2, "three": 3, "four": 4}
#add key_value pair
doors["five"] = 5
#updating/modifying
doors["five"] = 7
#delete use del()method
del doors["five"]
#.pp() method and clear() for entire dictionary
doors.pop("one")
#access a value from corresponding key
print(doors["two"])
print(doors)
"""
"""
#square of a number using while loop
number = eval(input("Enter a number:"))
while number <= 10:
    print("square is:",number ** 2)
    number = number + 1
    #breaks the loop
    if number == 5:
        break
"""
"""
#for loop
#start and stop the number to stop at is not included
for i in range(6, 18):
    print(i)
#break to stop loop,continue to continue
for number in range(1,10):
    print(number)
    if number == 8:
        break

"""
#function definition
def prep_night():
    print("it is raining to night")
prep_night()#calls the function
#returns a value
def ages():
    return 23
print(ages())
#parameter
def number(num, age):
    return("your number is:"  + str(num) + str(age))
print(number(23,67))