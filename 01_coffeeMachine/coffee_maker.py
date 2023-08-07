import data
from prettytable import PrettyTable


class CoffeeMaker:
    # constructor
    def __init__(self, input_resources):
        self.resources = input_resources
        """Build a Speisekarte"""
        self.table = PrettyTable()
        self.table.align = "l"
        coffee_list = []
        cost_list = []
        for menu in data.MENU:
            coffee_list.append(menu)
            cost_list.append("€" + str(data.MENU[menu]["cost"]))
        self.table.add_column("MENU", coffee_list)
        self.table.add_column("PRICE", cost_list)

    def print_table(self):
        print(self.table)

    def print_report(self):
        print(f"Remain\nWater: {self.resources['water']}\nMilk: {self.resources['milk']}\nCoffee: {self.resources['coffee']}\nMoney: €{str(round(self.resources['money']))}")

    def make_coffee(self, _order):
        self.resources['water'] -= data.MENU[_order]["ingredients"]["water"]
        self.resources['milk'] -= data.MENU[_order]["ingredients"]["milk"]
        self.resources['coffee'] -= data.MENU[_order]["ingredients"]["coffee"]
        print(f"Here, your {_order} ☕. Guten Appetit!")

    def cash_handling(self, _coffee_cost: float):
        success = False
        money = 0
        print(f"the price is: €{str(_coffee_cost)}")
        money += float(input("€0.10 coins: ")) * 0.10
        money += float(input("€0.20 coins: ")) * 0.20
        money += float(input("€0.50 coins: ")) * 0.50
        money += float(input("€1.00 coins: ")) * 1.00
        money += float(input("€2.00 coins: ")) * 2.00
        if money < _coffee_cost:
            return False, f"€{str(round(money, 2))}"
        else:
            self.resources['money'] += _coffee_cost
            return True, f"€{str(round(money - _coffee_cost, 2))}"

    def is_ingredients_sufficient(self, _order):
        sufficient = True
        error_report: str = "*** Insufficient amount of"
        water_ordered = data.MENU[_order]["ingredients"]["water"]
        milk_ordered = data.MENU[_order]["ingredients"]["milk"]
        coffee_ordered = data.MENU[_order]["ingredients"]["coffee"]
        if self.resources['water'] < water_ordered:
            error_report += f"\nwater, required {water_ordered} but remained {self.resources['water']}"
            sufficient = False
        if self.resources['milk'] < milk_ordered:
            error_report += f"\nmilk, required {milk_ordered} but remained {self.resources['milk']}"
            sufficient = False
        if self.resources['coffee'] < coffee_ordered:
            error_report += f"\ncoffee, required {coffee_ordered} but remained {self.resources['coffee']}"
            sufficient = False
        return sufficient, error_report

    def start(self):
        off = False
        """Get order from a customer"""
        valid = False
        while not valid:
            self.print_table()
            order = input("What would you like? (espresso, latte, cappuccino): ")
            if order in data.MENU:
                valid = True
            elif order == "off":
                off = True
                valid = True
            elif order == "report":
                print(self.print_report())
            else:
                print("Sorry, we do not have that")

        if not off:
            """make coffee"""
            is_ingredients_sufficient_output = self.is_ingredients_sufficient(order)
            if is_ingredients_sufficient_output[0]:
                """take money"""
                valid = False
                while not valid:
                    cash_handling_output = self.cash_handling(data.MENU[order]['cost'])
                    if cash_handling_output[0] is False:
                        print(f"Insufficient money, return {cash_handling_output[1]}")
                        print(f"Please try again")
                    else:
                        valid = True
                print(f"Transaction success, exchange {cash_handling_output[1]}")
                self.make_coffee(order)
            else:
                print(is_ingredients_sufficient_output[1])
            print(self.print_report())
            self.start()
