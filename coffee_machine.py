from ingredients import MENU

QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01

class Coffee:
    def __init__(self, menu):
        self.water = 300
        self.milk = 200
        self.coffee = 100
        self.menu = menu

    def coins_cost(self, choose_drink, total):
        cost = {"espresso": 1.5,
                "latte": 2.5,
                "cappuccino": 3.0}
        if total > cost[choose_drink]:
            your_change = float(total) - cost[choose_drink]
            print(f'Drink ready. Here is your {choose_drink}\nYour change:{your_change}')
        elif total == cost[choose_drink]:
            print(f'Drink ready. Here is your {choose_drink}\nYour change:0')
        else:
            print("not enough money")

    def drink_resources(self,choose_drink):
        if choose_drink == "report":
            print(f'water { self.water}\n'
                  f'milk {self.milk}\n'
                  f'coffee: {self.coffee}')
        else:
            drink = choose_drink
            water = self.water - self.menu[drink]["ingredients"]["water"]
            milk = self.milk - self.menu[drink]["ingredients"]["milk"]
            coffee = self.coffee - self.menu[drink]["ingredients"]["coffee"]

            if self.menu[drink]["ingredients"]["water"] <= self.water:
                if self.menu[drink]["ingredients"]["milk"] <= self.milk:
                    if self.menu[drink]["ingredients"]["coffee"] <= self.coffee:
                        self.water = water
                        self.milk = milk
                        self.coffee = coffee
                        return 0
                    else:
                        return 1

    def play_game(self):
        machine_working = True
        while machine_working:
            choose_drink = input("what would you like? (espresso/latte/cappuccino): ").lower()
            if choose_drink == "off":
                machine_working = False
            else:
                if choose_drink == "espresso" or "Latte" or "cappuccino" or "report":
                    drink = Coffee(MENU)
                    drink_value = drink.drink_resources(choose_drink)
                if drink_value == 1:
                    print("not enough resources")
                elif drink_value == 0:
                    quarters = int(input("how many quarters: ")) * QUARTERS
                    dimes = int(input("how many dimes: ")) * DIMES
                    nickles = int(input("how many nickles: ")) * NICKLES
                    pennies = int(input("how many pennies: ")) * PENNIES
                    total = quarters + dimes + nickles + pennies
                    drink.coins_cost(choose_drink,total)



coffee = Coffee(MENU)
coffee.play_game()