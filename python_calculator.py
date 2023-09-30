def addition(a, b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        print("Can't divide by zero")
        return 0
    else:
        return a / b


while True:
    print("\nSelect Operation")
    print("q. Quit")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = (input("Enter your choice: "))
    if choice == 'q':
        print("Goodbye")
        break
    
    if choice in ['1','2','3','4']:
        num1 = float (input("Please enter fist number: "))
        num2 = float (input("Please enter sccond number: "))
        
    if choice == '1':
        result = addition(num1,num2)
        print("Your result is: ", result)
        
    elif choice == '2':
        result = subtract(num1,num2)
        print("Your result is: ", result)
        
    elif choice == '3':
        result = multiply(num1,num2)
        print("Your result is: ", result)

    elif choice == '4':
        result = divide(num1,num2)
        print("Your result is: ", result)

    else:
        print("invalid input")