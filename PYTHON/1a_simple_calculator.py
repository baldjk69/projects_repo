
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
operation = input("Do you want to [Add / Subtract / Multiply / Divide] : ")

def add(a, b):
    return a+b
    
def subtract (a, b):
    return a-b
    
def multiply(a, b):
    return a*b
    
def divide(a, b):
    return a/b  
    
if operation == "add" :
    print(add(a, b))

if operation == "subtract" :
    print(subtract(a, b))
    # TODO: write code...
    
if operation == "multiply" :
    print(multiply(a, b))    

if operation == "divide" :
    print(divide(a, b))

    
    

