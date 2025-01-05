# Python data types
"""
to know the type of the data type use type()

String 
Numbers - Integers and Float
Boolean 
List
Tuple
set 
dict 
None    
    
"""
print(type(1)) # <class 'int'>


# STRING

# defined either in single or double quotes
# you can also use the inbuilt string constructor str()
#          str("I am a string") - though this is not common

dog_name="Miles" # miles is the string
print(dog_name)

#using strings together with variables use f string f"{varible_name}"
price_1="2.5"
price_2=2.5

print(f"The total price is {price_1}")
print(f"The total price is ${price_2:.2f}") #this works with numbers and doesnt work with price_1 (string)


#some python methods
"""
    to see the available methods use dir()
    
    Everything in python is an object 
    All of the methods that we called on strings above are available because the string literal "hello" is an instance of the String class. 

    """
print(dir("hello"))    
var_1="hello"
print(var_1.capitalize())
print(var_1.lower())
print(var_1.upper())
print(var_1.strip()) #strip removes the extra space ahead
print(var_1.startswith("h")) #if it starts with the specified letter it returns True else false




