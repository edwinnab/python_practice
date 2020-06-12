#shows the title
print("Tip Calculator");
print("Kindly enter your total bill in Ksh:");
bill = int(input());
#defines the type of services
print("x=good services,y=great services,z=terrible services");
x = 0.15
y = 0.20
z = 0
print("Enter your level of s:");
s = input();
#calculates the tip percentage
tipx = (0.15*bill)
tipy = (0.20*bill)
tipz = (0.00*bill)
#calculates total cost
costx = (bill+tipx);
costy = (bill+tipy);
costz = (bill+tipz);
print("your total costx:", +costx, "your total costy:", +costy, "your total costz:", +costz);
