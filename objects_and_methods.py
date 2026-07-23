# Let's first re-create a variable or two
my_integer = 10
my_str = "Hello world"
# You can use the type() function to check the type of a variable
type(my_integer) #This will return <class 'int'>
type(my_str) #This will return <class 'str'>

#What is stored inside these objects
my_str.upper #Upper is a METHOD that is attached to all the objects of class string
#A method is like a function, so it needs to be CALLED putting () after.
my_str.upper() #Returning the upper, capitalized version of the string.
my str.upper() #What does it mean to return a copy?
#it means the original string is unchanged:
my_str
#Trying other methods:
my_str.lower()
#What else?
my_str.endswith('!') #Returns False because the string does not end with '!'
my_str.endswith('orld') #Returns True because the string does end with 'orld'
#Methods are a way of pairing functions with the objects they are meant to work on. 

#Some objects have other things besides methods: properties
#Properties are information abot theobject that was created.
my_integer.denominator #White wrenches are properties of the object
my_integer.numerator #Returns 10, the numerator of the integer
#Properties are only meant to be read. They dont do anything. They just exist
#If something does not require a calculation to be given, it is a property. Look at the icon to check

