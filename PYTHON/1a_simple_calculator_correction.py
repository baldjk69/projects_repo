
a = float(input("Enter the first number : "))
b = float(input("Enter the second number : "))
operation = input("Do you want to [Add / Subtract / Multiply / Divide] : ").lower()

def add(a, b):
    return a+b
    
def subtract (a, b):
    return a-b
    
def multiply(a, b):
    return a*b
    
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a/b  
    
if operation == "add" :
    print("Result: ",add(a, b))

elif operation == "subtract" :
    print("Result:", subtract(a, b))
    
elif operation == "multiply" :
    print("Result: ", multiply(a, b))    

elif operation == "divide" :
    print("Result: ", divide(a, b))
    
else:
    print('Invalid operation')

    
    

