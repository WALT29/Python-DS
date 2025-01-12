import random
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

# NUMBERS
"""
There are 3 types of numbers 
    Integers -7 
    Float - 8.3
    complex - ij

You can convert other data types to float / int using float () and int()

"""

# to generate random numbers use (import random) python doesnt have random() function
print(random.randrange(1,40))

#SEQUENCE TYPE
"""
1)LISTS
2)TUPLES
3)SETS
4)DICTS

"""

#LISTS
"""
[1,2,3,4,5]
You can create a list using the list() syntax
list() - will create an empty list

accessing an element in the list you should know the index of the element.Index starts from 0

"""
my_list=["a","b","c","d"]
print(my_list[1])

list2=[1,2,3,4,5,6,7]
print(list2.pop()) # removes the last element in the list and returns the element that has been removed

list2.remove(1) # removes the specified element
print(list2)

print(sorted([23,45,1,2,56,8])) # sorted arranges the elements in the right order by default in the ascending order


"""
working with SORT

        it sorts the list in ascending by default 

        list.sort(reverse=True|False,key=myFunc)

    parameter values - optional
    
        reverse- reverse=True will sort the list in descending order ,default is reverse=False
        
        key-A function to specify the sorting criteria    
"""
#sort the list by descending
nums=[1,3,4,5,2,0]
nums.sort(reverse=True)
print(nums)

cars=['BMW','FORD','BENZ','VOLVO']
cars.sort(reverse=True)
print(cars)


#sort the list by length
cars2= ['Ford', 'Mitsubishi', 'BMW', 'VW']

def myFunc(element):
    return len(element)

cars2.sort(key=myFunc)
print(cars2)

"""
WHY NO ARGUMENTS ARE PASSED EXPLICITLY TO MY FUNCTION (myFunc)

    when using key=myFunc you are not  calling the function urself.Instead you are passing the functon object(not the result of the function ) to the sort() method
    sort method automatically applies the function to each element of the list so you dont need tp explicitly pass anything
    
    its like saying "he sort " here is my function use it to calculate the sorting keys for each item in  the list
"""

#sort by year 
cars3= [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

def myFunc2(element):
    return element['year']

cars3.sort(key=myFunc2)
print(cars3)

#sort by length

cars3.sort(key=lambda element:len(element['car']))

print(cars3)


# TUPLES
"""
    Tuples are created with closed and opened parenthesis ()
    tuple() - class constructor function can be used to cast list and other iterable data types to tuples 
    Tuples are immutable - once a tupple has been created it cannot be changed
        NB: Tuples dont have methods like pop() or insert()
    
    While tuples are less flexible ,they can be advantageous .Tuples can be used in data retrieved from the database.The tuple protects the data until its no longer needed
    
    NB:Parentheses can also be used to order of operations and grouping of statements.To let python know its working with a tupple ,there has to be at least one comma even when there is one element in the tuple
    (1,)
    
"""
myL=[1,2,3,4]
myl2=[1]
print(tuple(myl2))

# SETS AND DICTS

#SETS
"""
{}
A set is unindexed,unordered and unchangeable 
can be initiated with curly brackets or the set() class constructor

set () class constructor takes a list / tuple as its on argument
the elements of a set are unique

UNINDEXED - means that we cannot access elements of the set using square brackets as we do in  list

UNORODERED - means elements of a set are in a random order

UNCHANGEABLE - means the individual elements of a set cannot be changed

NB:A set is not immutable because its overall structure can be changed ,it can be changed it  be made shorter or longer(yaani you can add more things in the set).Its unchangeable because an element cannot be changed into something else 

sets have many of the same methods as lists

"""

my_set=set(['3','2','3','a','b','a'])
print(my_set)

s={1,2,3,4,5}
s.pop() # pop reomves an element at a specified position pop(1)
s.remove(3)
print(s)

#Dictionaries
"""
composed of key/value pair
    {"key":value}
    keys must be in string format
    
can be created using the dict() class constructor

To access data in the dictionary ,you canuse the square bracket notation [] and pass in the key you are trying to access
    dictionary["key"]

you can also use the built in .get() method to retrieve the value of the key.
    this is useful sometimes when you are unsure if a key exists as it returns None instead of an error it no matching key exists

"""
dict2=dict(x=1,y=2)
print(dict2)
my_dict={
    "key1":1,
    "key2":2
}
print(my_dict['key1'])
print(my_dict.get("key2"))
print(my_dict.get("key3")) # .get() is good when you dont know if the key exists 

#None
"""
None represents absence of value


In JS there are 2 diff types of representing absence of value : null and undefined
    UNDEFINED - comes up when:
        - when a variable has been created but has not been assigned a value 
        - when a function does not return a value
    
    NULL -Signifies the absence of any value

Unlike Js python wont allow you create a variable without assigning a value 

you must explicitly assign the value of NONE

"""
no_value=None
print(no_value)

# BOOLEAN
"""
There are two values of boolean data type - True and False

"""
##Types of errors
"""
Syntax Errors - These errors are a result of incorrect syntax

Logic Errors- These errors are hard to find they are not perceived as errors by the python interpreter
    - To find a logic error a programmer must comb thru the code line by line
    
Exceptions - Exeception pop up when the interpreter knows what to do with the piece of code but is unable to complete the action
    - The main difference with the other errors is that when the interpreter encounters an exception it can continue reading the application ,you just tell it what to except
    
    TYPES OF EXCEPTION
        ASSERTIONERROR
            -An assert() tells the interpreter the code inside of it must proceed without exeception or error ,if an assertion fails an assertionerror is raised
                EG
                assert(1==2)


        INDEXERROR & KEYERROR
            -Index error arises when trying to access an element at an index past the end of the list
                EG
                list=[0,1,2,3,4]
                print(list[10])
            -Key errors relate to dict.if a key is referenced but does not exist
                EG
                dict4={'a':1,'b':2}
                print(dict4['d'])
                

        
        NAMEERROR
            -A name error arises when a name is referenced before it has been defined 
        
        TYPEERROR
            - Arises when an operation or function is applied to an object of the wrong type
                EG
                wrong_type="abc"+123
                 
"""



















