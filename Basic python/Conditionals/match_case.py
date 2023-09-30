n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
op = input("Enter operator: ")
match op:
    case "+" :
        print(n1 + n2)
    case "-":
        print(n1 - n2)
    case "*":
        print(n1 * n2)
    case "/":
        print(n1 / n2)
    case _:
        print("Enter a valid operator")