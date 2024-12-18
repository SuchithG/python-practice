#List Manipulation:

#Create a list of Kannada foods. Use list comprehension to create a new list where each food name is in uppercase.

kannada_foods = ["uppitu", "bisibelebath", "palav", "idli", "dose", "chithranna"]

uppercase_food_names = [ up_fd_nme.upper() for up_fd_nme in kannada_foods]
print(uppercase_food_names)