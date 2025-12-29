import random
print("             WELCOME TO MY GUSSING GAME  👾                                           ")
print("==================================================")
a=int(input( "Enter a Number between 1 to 15 ------> "))
print("==================================================")
b=random.randint(1,15)
print(" Game Generated Number :",b)
if(a==b):
    print(" 🎉 Hurray You Win . ")
else:
    print(" 🤦 Sorry You Loose ")
print("==================================================")
print("Try Your Luck Again 👍")
