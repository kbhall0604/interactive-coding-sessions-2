#Advanced topics in loops

#Starting with iterables.
#We have seen that we can loop over lists with for loops:

for 1 in [1, 2, 3, 4]:
    print(i)

#We can loop with for over ANYTHING that is iterable:
#Like a string

for l in "Hello world":
    print(l) #We get the characters one at a time:

#We already knew that strings are iterable from:
my_name = "Katherine"
my_name[0:4]

#What ekse can we iterate on?
my_info = {"name": "Katherine",
           "age": 22,
           "city": "Boulder"}

for k in my_info:
    print(k) #Going to get the keys

    #Iterating over the dict returns the keys. So how do we get the value?

for key in my_info:
    print(f"The current key is {key}, and its associated value is {value}.") #How do we get this value

my_info["name"]
my_info["age"]
my_info["city"]

#It would be better if we could get both the key and the value when iterating over a dictionary:
my_fruits = ['banana', 'apple', 'mango']
first_fruit, second_fruit, third_fruit = ["banana", "apple", "mangoo"]
name, age, city = "Katherine", 22, "Boulder"
#Unpacking
print(first_fruit)

#Let's return to the dictionary
my_info.items()

for (key, value) in my_info.items():
    print(f"The key is {key}, and associated value {value}")

#lets revisit how to loop on my name
my_name = "Katherine"
for letter in my_name:
    print(letter)

#I would like to know the index of each letter in my name. What are the letters position?
#Whenever this question is asked, use: enumerate()
#How does it work:
for (index, letter) in enumerate(my_name):
    print(f"The letter at position {index} is {letter}")

#The only thing to do is replace iterable by enumerate(iterable)
#replace step_variable by (index, step_variable)
#You can use any variable name that you'd like bu the first one will recieve the index, the second element itself.

a_list_of_food = ["pickle", "pepper", "peach"]
a_list_of_tastes = ["sour", "spicy", 'sweet']

#You can iterate over two (or multiple) lists in parallel
#First zip them
for (food, taste) in zip(a_list_of_food, a_list_of_tastes):
    print(f"A {food} tastes {taste}.")

#What if we also had color?
a_list_of_colors = ["green", "red", "orange"]
for (food, taste, color) in zip(a_list_of_food, a_list_of_tastes, a_list_of_colors):
    print(f"A {food} tastes {taste}. and is {color}")

#The first thing to cover is a small utility to create lists of numbers to loop on
#What if we were printing all sqaures between 0 and 1000:
#So far we did something like:
list_of_numbers = [0, 1, 2, 3, 4, 1000] #This is not ideal
#Range = a large lsit of numbers to loop on
for i in range(1000):
    print(i**2) #This is a lot of numbers to print, but it works
#It takes one argument called stop: The value at which you will stop.
#This is the same as for i in [0,1,2,3,...,999]: print(i**2)
#You can also give two other arguments to range: start and step
for i in range(3, 10, 2):  
    print(i)
#The start, stop, and step are things we've seen before in slicing. They work the same for range 
#Except they create an interval rather than slicing the values in an existing iterable
for i in range(5,30,5):
    print(i)

#Now for something a little more complicated
#Lets say we want to generate a list of all the squares of numbers 1-9
#We do that using a for loop
squares = []
for i in range(1,10):
    square = i**2
    squares.append(square)
print(squares)
#We built a list one element at a time using a for loop
#When you have to build a list (or any interable) for another list you will often encouter a LIST COMPREHENSION
#It is simply a for loop, written in a more concise way, that builds a list

squares = [i ** 2 for i in range(10)]
#A list comprehension starts with square brackets, after all we are buidling a list
#Then an expression comes: here, its (i ** 2) it tells us what each element of the list will be
#Then comes the for loop, FOR STEP_VARIABLE IN ITERABLE. No colon, that's all

#Another example:
first_name = 'Katherine'
whats_this = [x.upper() for x in first_name]
print(whats_this)

#You can add another "bell" to a list comprehension- certain elements can be filtered

#We want to get the squares of all numbers between 0 and 9, but only if the sqaure is less than 30.
small_squares = [i ** 2 for i in range (0, 10) if i ** 2 <30]
#This is the same list comprehension as before EXCEPT there's an IF statement.
#The IF statement conditions whether the element will be added to the list or not. If the condition is 
#False the element is not added but if it is true than it will be added
print(small_squares)

# Let's say you have a messy folder. Your colleague is managing a messy folder

folder_content = ["data.csv", "report.pdf", "summary.csv", "image.png", "notes.txt", "data2.csv", "archive.zip"] 
#What I want: filter all elements that not .csv files
#Reminder: You can check if a file ends with .csv by using the string method .endswith()
#Here is a list comprehension that filters the .csv files from the folder content

filtered_csv_files = [file for file in folder_content if file.endswith(".csv")]
print(filtered_csv_files) #['data.csv', 'summary.csv', 'data2.csv']
