# Basic variable & print
message = "Hello World!"
print(message)

# f-string (formatted string literal)
print(f'{message}')

# String concatenation
hello = "Hello "
world = "World!"

print(hello+world)

# Direct print
print("Hello World!")

# Using multiple arguments in print (comma)
print("Hello", "World!")

# Using string multiplication 
print("Hello " * 1 + "World!")

# With escape characters (line, tab, quotes)
print("Hello\nWorld!") # New Line
print("Hello\tWorld!") # Tab
print("He said \"Hello World!\"")

# Using join()
print("".join(["Hello ","World"]))

# Using a function
def say_hello():
    return "Hello World!"
    
print(say_hello())  

# From a list
words = ["Hello ","World!"]
print("".join(words))
