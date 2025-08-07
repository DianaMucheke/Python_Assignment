number_1 = int(input("Enter first number:"))
number_2 = int(input("Enter second number:"))

operation = input ("Enter mathematical operation (+,-,/,*)")

if operation == "+":
    sum = number_1 + number_2
    print(sum)
elif operation == "-":
    difference = number_1 - number_2
    print(difference)
elif operation == "/":
    division = number_1 / number_2
    print(division)
else :
    multiplication = number_1 * number_2
    print(multiplication)
