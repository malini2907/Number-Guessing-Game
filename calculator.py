def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

while True:
    print("\nPlease select operation -\n") 
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit \n")

    i = input("Select operation from 1, 2, 3, 4, 5: ")

    if i == '5':
        print("Exit the calculator.")
        break
    elif i in {'1', '2', '3', '4'}:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if i == '1':
                print(add(a, b))
            elif i == '2':
                print(subtract(a, b))
            elif i == '3':
                print(multiply(a, b))
            elif i == '4':
                    print(divide(a,b))
