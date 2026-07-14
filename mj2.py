name = input("Enter name:")
age = int(input("Enter age "))
hight = int(input("Enter hight (cm) :"))
power = int(input("Enter your power score (1-10):"))
dollar = int(input("Enter your starter pack dollar (1 - 100): "))

print("======")
if power >= 9 and dollar >= 80 and age >= 30 :
    print("You are pass")
    print("You are head of team")
elif power >= 6 and dollar >= 60 and age >=30 :
    print("You are pass")
    print("You are vice of the team")
elif power >= 3 or dollar >=30 and age >=19 :
    print("You are pass")
    print("You are member of the team") 
else :
    print("Nah never go away")