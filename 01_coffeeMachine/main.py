import data

# initialize
resources = data.resources


def print_report():
    print(f"Remain\nWater: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: €{str(round(resources['money']))}")


def make_coffee(_order):
    resources['water'] -= data.MENU[_order]["ingredients"]["water"]
    resources['milk'] -= data.MENU[_order]["ingredients"]["milk"]
    resources['coffee'] -= data.MENU[_order]["ingredients"]["coffee"]
    print(f"Here, your {_order} ☕. Guten Appetit!")


def cash_handling(_coffee_cost: float):
    success = False
    money = 0
    print(f"the price is: €{str(_coffee_cost)}")
    money += float(input("€0.10 coins: "))*0.10
    money += float(input("€0.20 coins: "))*0.20
    money += float(input("€0.50 coins: "))*0.50
    money += float(input("€1.00 coins: "))*1.00
    money += float(input("€2.00 coins: "))*2.00
    if money < _coffee_cost:
        return False, f"€{str(round(money, 2))}"
    else:
        resources['money'] += _coffee_cost
        return True, f"€{str(round(money - _coffee_cost, 2))}"


def is_ingredients_sufficient(_order):
    sufficient = True
    error_report: str = "*** Insufficient amount of"
    water_ordered = data.MENU[_order]["ingredients"]["water"]
    milk_ordered = data.MENU[_order]["ingredients"]["milk"]
    coffee_ordered = data.MENU[_order]["ingredients"]["coffee"]
    if resources['water'] < water_ordered:
        error_report += f"\nwater, required {water_ordered} but remained {resources['water']}"
        sufficient = False
    if resources['milk'] < milk_ordered:
        error_report += f"\nmilk, required {milk_ordered} but remained {resources['milk']}"
        sufficient = False
    if resources['coffee'] < coffee_ordered:
        error_report += f"\ncoffee, required {coffee_ordered} but remained {resources['coffee']}"
        sufficient = False
    return sufficient, error_report


while True:
    """Get order of a customer"""
    valid = False
    while not valid:
        order = input("What would you like? (espresso, latte, cappuccino): ")
        if order in data.MENU:
            valid = True
        elif order == "off":
            exit()
        elif order == "report":
            print(print_report())
        else:
            print("Sorry, we do not have that")


    """make coffee"""
    is_ingredients_sufficient_output = is_ingredients_sufficient(order)
    if is_ingredients_sufficient_output[0]:
        """take money"""
        valid = False
        while not valid:
            cash_handling_output = cash_handling(data.MENU[order]['cost'])
            if cash_handling_output[0] == False:
                print(f"Insufficient money, return {cash_handling_output[1]}")
                print(f"Please try again")
            else:
                valid = True
        print(f"Transaction success, exchange {cash_handling_output[1]}")
        make_coffee(order)
    else:
        print(is_ingredients_sufficient_output[1])
    print(print_report())


