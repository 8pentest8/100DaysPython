from coffee_machine_menu import menu, resources

work_coffee_machine = True
money = 0


def is_resources(order_indr):
        for item in order_indr:
            if order_indr[item] >= resources[item]:
                print(f"Sorry there is not enough {item}")
                return False
        return True


def proc_coins():
    print("Please insert coins")
    total = int(input("How many quaters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many qnickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def transaction_successful(money_receive, drink_cost):
    if money_receive >= drink_cost:
        change = round(money_receive - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money +=money_receive
        return True
    else:
        print("Sorry that`s not enjugh money. Money refunded.")
        return False


def make_coffee (drink_name, order_ingred):
    for item in order_ingred:
        resources[item] -= order_ingred[item]
    print(f"Here is your {drink_name} ☕")


while work_coffee_machine:
    offer = input("What would you like? Choose and enter some of them in brackets (espresso/latte/cappuccino): ").lower()
    if offer == "report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['water']}g\nMoney: ${money}")
    else:
        drink = menu[offer]
        print(f"You choose {offer}, {offer} has next ingredients: water - {menu[offer]['ingredients']['water']}, milk - {menu[offer]['ingredients']['milk']}, coffee - {menu[offer]['ingredients']['coffee']}g It is cost: ${menu[offer]['cost']}")
        if is_resources(drink['ingredients']):
            payment = proc_coins()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(offer, drink['ingredients'])