from calculator_art import logo

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    try:
        num1 = float(input("What's the first number?: "))
        for symbol in operations:
            print(symbol)
        should_continue = True
        while should_continue:
            operation_symbol = input("Pick an operation: ")
            num2 = float(input("What's the next number?: "))
            try:
                function = operations[operation_symbol]
                result = function(num1, num2)
                print(f"{num1} {operation_symbol} {num2} = {result}")
                need_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or type 'q' to quit: ")
                if need_continue == "y":
                    num1 = result
                elif need_continue == "n":
                    should_continue = False
                    calculator()
                elif need_continue == "q":
                    should_continue = False
                else:
                    print("You enter incorrect value! Your session closed!")
                    should_continue = False
            except KeyError:
                print("You enter incorrect operation symbol!")
    except ValueError:
        print("You enter incorrect value!")
calculator()


