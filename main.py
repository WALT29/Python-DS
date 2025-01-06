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

        its sorts the list in ascending by default 

        list.sort(reverse=True|False key=myFunc)

    parameter values - optional
    
        reverse- reverse=True will sort the list in descending order ,default is reverse=True
        
        key-A fucntion to specify the sorting criteria
        
    
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
Tuples are immutable - once a tupple has been created it cannot be changed 
"""