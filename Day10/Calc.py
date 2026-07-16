from art import logo
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    status = True
    print(logo)
    number1 = float(input("What's your first number?: "))
    while status:
        for symbol in operation:
            print(symbol)
        operator = input("Pick an operation: ")
        number2 = float(input("What's the next number?: "))
        solution = operation[operator](number1, number2)
        print(f"{number1} {operator} {number2} = {solution}")
        choice = input(f"Type 'y' to continue calculating with {solution}, or type 'n' to start new calculation: ").lower()
        if choice == "y":
            number1 = solution
        else:
            status = False
            print("\n"*20)
            calculator()
calculator()
