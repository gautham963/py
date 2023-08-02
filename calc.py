print("This is a sample calculator program")

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

op = input("Operation required to be done: ")

match op:
    case "+":
        print("The sum of numbers is: ",number1+number2)

    case "-":
        print("The subtaction of numbers is: ",number1-number2)

    case "*":
        print("The multiplication of numbers is: ",number1*number2)

    case "/":
        print("The div of numbers is: ",number1/number2)
