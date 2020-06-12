import random #imports the module random
print("What's your question:");
question = input();#takes input from user
num = random.randint(0,10);#creates a random integer
if num<=8:
    print("YES");
elif num<8:
    print("NO");
else:
    print("Ask another question");
