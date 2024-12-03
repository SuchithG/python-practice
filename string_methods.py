# String methods
message = " Hello world!"
print(message.lower())  # Output: hello world!
print(message.upper()) # Output: HELLO WORLD!
print(message.replace("world", "python")) # Output: Hello python!

# Escape Sequences
print("Hello\nWorld!") # Output: Hello
                       #         World!
print("Hello\tWorld!") # Output: Hello   World!
print("Hello\\World!") # Output: Hello\World!

# String repetition methods
greeting = "Hello\t" * 3 # Output: Hello   Hello   Hello
print(greeting)

# String concatenation 
first_name = "John"
last_name = "Wick"
print(first_name + " " + last_name) # Output: John Wick

# Indexing string
text = "Python"
print(text[4]) # Output: o
print(text[-1]) # Output: n

# Slicing String
text = "Python Programming"
print(text[0:6]) # Output: Python
print(text[:6]) # Output: Python
print(text[7:]) # Output: Programming
