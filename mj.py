quantity = int(input("Enter amount :"))
cost_price = float(input("Enter cost price :"))
sell_price = float(input("Enter sell price :"))
team_member = int(input("Enter team member :"))

cost = quantity * cost_price 
sell = quantity * sell_price
money = sell -  cost  
money_boss = money * (20/100)
money -= money_boss
team_money = money / team_member
print("Amount cost",cost,"Bath")
print("Sell cost",sell,"Bath")
print("Overall money",money,"Bath")
print("money for boss",money_boss,"Bath")
print("team money per person",team_money,"Bath")
