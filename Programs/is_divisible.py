num = int(input("enter a positive integer: "))
# if num%5 == 0:
#     print("number is divisible by 5")
# elif num%15 == 0:
#     print("number is divisible by 15")
# elif num%3 == 0:
#     print("number is divisible by 3")
# else:
#     print("number is not divisible by 5 or 3 or 15")

if num%15 == 0:
    print("number is divisible by 15")
else:
    if num%5 == 0 or num%3 == 0:
        print("number is not divisible by 15 but divisible by 5 or 3")
    else:
        print("the number is not divisible by 5, 3 or 15")  