print("Hello World") #In our python file (also called a Python script).
print("Hello friends") #Final way of running python code: Run a script in full.

#What are the variables in Python?
this_string = "Katherine" #This is a string.
#I assigned the value "Katherine" to to the variable this_string
#This operation does not return anything.

this_float = 3.14 #This is a float
this_int = 12 #This is an integer
this_bool = False #Note the case-sensitive

#What can you do with variables?
#Only after the line is executed do the variables exist in Python's memory.
print(this_float) #Tab to autocomplete the current selection
print(this_string)

#What else can you print?
print(this_string) #You can print a variable
print("Hello") #You can print a 'literal
print(12) #You are not storing it into a variable, you are directly printing an input.
print(12 + 5) #Printing an expression.
#SKILL: Being able to 'trace the code'. Meaning reconstruct the steps of a code.
#Another example of an expression:
print(this_float +5) #Here, we can trace the steps again

#What is print()?
#print() is a function. A function is a way of doing something in python.
# Functions are 'called' using ()
# Functions take a numbre of arguments (what goes inside the parentheses).
# Some functions take zero, others take many.

#How many arguments does print() take?
# It can take one
print(this_float)
# ...but it can take more
print(this_float, this_int, this_string)
#Print is printining all of its arguments on the same line.

#Lets do calculations
print(2+3)
print(2*5)
print(2 + 3 * 5)
print( (2+3) * 5)

print(0.1 + 0.2)
print((0.1 +0.2) == 0.3)
# Floating point error. Operations with decimal numbers are, by default, not mathematically 'exact'

#How can we avoid this?
#One way is to round:
my_rounded_sum = round(0.1 + 0.2, 2)
print(my_rounded_sum == 0.3) #True


#More logical comparisons:
print(1<2)
print(1>2)
print(1>=2)
print(1<=2)
print(1 != 2)

# You can also create more complex comparisons:
print((1 < 2) and (3 > 2))
condition_1 = True
condition_2 = True
condition_3 = False
condition_4 = False
print(condition_1 and condition_2) #Both True
print(condition_1 and condition_3) # False, so True
# AND requires ALL conditions to be True
#What about or?
print(condition_1 or condition_2) #True, because at least one is True
print(condition_1 or condition_3) #True, because at least one is True
#This is VERY important to understand!!

print(False + False)
print(False + True)
print(True + True)
print(True ==1)
print(False == 0)

print(False*5)
print(True*3+1) #Simple stand ins for 0 and 1.

greeting = "Hello" + "world!"
print(greeting) #The meaning of '+' changes when applied to a string
# +, when applied to strings, is called concatenation. It joins two strings together.

laugh = "ha" * 3
print(laugh) #This is called a repetition operator. It repeats the string a number of times.

weird_laugh = "ha" * 3.14 #does not work because the repetition operator only works with integers.

my_age = 22
my_intro = "I'm Katherine and I'm " + my_age + " years old." #This does not work because you cannot concatenate a string and an integer.
#Returns a TypeError.
#When you want types to work nicely with each other, you need to convert them to the same type.

#Here are type conversions:
my_age_as_a_str = "22"
my_intro = "I'm Katherine and I'm " + my_age_as_a_str 
print(my_intro) #This works because both are strings.

#A better way to do that is to convert one type to the other
#These 4 functions can be used: str(), int(), float(), bool()
print(str(22))
#Is this really a string? Let's check:
type(str(22))
#Let's try others
str(3.14)
str(False)
str(0.1 + 0.2)
#We can convert anything to a string: int, bool, float

#Let's try float:
float('Hello')
float('32')
float(False)
float(40)
float('fifteen')
#For float it sometimes works, but not always.

#Now int:
int('Hello')
int(True)
int('32')
int(3.14)
int(3.6) #As we can see, int() cuts off the decimal part of a float, it does not round it.

#Another great skill: Running experiments on your code,
