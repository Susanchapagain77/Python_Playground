def add(n1, n2):
    """function to add values"""
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator():
    while True:
        num1 = float(input("1st number: "))
        num2 = float(input("2nd number: "))

        def print_operations():
            for key in operations:
                print(key)

        print_operations()
        opn = input("which operation do you want to perform? ")
        fxn = operations[opn]
        result = fxn(num1, num2)
        print(result)

        while True:
            choice = input(f"Do you want to perform another operation with {result}? (y/n) or press q to quit the program ").lower()
            if choice == 'n':
                calculator()
            elif choice == 'y':
                print_operations()
                opns = input("which operation do you want to perform? ")
                num3 = float(input("3rd number: "))
                result = operations[opns](result, num3)
                print(result)
            else:
                return False;

calculator()
