#If statements are about defining when or whether a block of code will run
#loops are about defining how many times a block of code will run.
#Its about doing the same operations multiple times.
#Learning two types of loops today: 

#1. While loops
#While keyword, followed by LOGICAL statement, followed by colon:
#1. Initialize the parts of the logical statement.
count = 0 #The count exists, it has been defined. We initialized the condition
while count < 5:
    count = count + 1 #Prevents the loop from running forever.  Avariable that enters the condition is changing
    print(count)
#Inside there is a code block again
#The second thing that a while loop needs is the content of the logical statement might change. 
#Otherwise it might loop forever
#understand what happens at each iteration of the loop and how many times it runs

#iteration #, count
#First iteration, 1
#Second iteration, 2
#Third iteration, 3
#Fouth iteration, 4

#Second related skill:
#Predicting how many times a loop will run
#Here is a more realistic example of a while loop:

user_input = ""
while user_input == "":
    user_input = input("Please type something:")
    print("The user typed:" + user_input)

#Another example: A to-do list, but first, here is a useful trick

age = 22
name = "Katherine"
school = "CU Boulder"
message = "My name is" + name + ", I am" + str(age) + "Years old, and I teach at" + school
#How to combine with text but it's of a PITA to write.
#Use 'f-strings' to simplify
better_message = f"My name is {name}, I am {age} years old and I teach at {school}"
print(better_message)

#Back to loops!
#A while loop with a to-do:
to_dos = ["Walk the dog", "mow the lawn", "take out the trash", "do the dishes"]
while len(to_dos) ! = 0:
    item = to_dos.pop() #.pop() takes out the last element of the list, modifying it in place, and returns it
    print(f"Im doing this: {item}. I still have these to do: {to_dos}")

#Lets try tracing the loop:
#Iteration #, item, to_dos:
#First iteration, 'do the dishes', ["walk the dog", "mow the lawn", "take out the trash"]
#Second iteration, 'take out the trash', ["walk the dog, "mow the lawn"]
#Third iteration, 'mow the lawn', ["walk the dog"]
#Fourth iteration, 'walk the dog', []

#ANOTHER COMMON GOTCHA
#The second type of loops: FOR LOOPS
list_of_numbers = [1, 2, 3, 4, 5]
for i in list_of_numbers:
    print(i)

#Anatomy of a FOR loop:
#It starts with for
#Immediately after for is a variable name.
#It can be anything
#Here is is i, but I could call it a number, n, x, a...
#This variable is called the STEP variable. It will take a different value at each loop
#Then the keyword in
#Then an iterable: Any collection of items: Here, it is a list.

list_of_numbers = [1, 2, 3, 4, 5]
for i in list_of_numbers:
    print(i)
#The for loop iterates over the elements of the iterable
#Storing each element into the STEP variable at each loop

#Lets consider a slightly more complex for loop: we have a list of numbers and we want to print their square:
list_of_numbers = [2, 3, 4, 5]
for number in list_of_numbers:
    square = number **2
    print (f"The square of {number} is {square}")
#Trace loop before we run it:
#Iteration #, number, square
#First iteration, 2, 4
#Second iteration, 3, 9
#Third iteration, 4, 16
#Fifth iteration, 5, 25

#Now, making things more complex:
#All of the squares are printed but they haven't been stored anywhere

list_of_numbers = [2, 3, 4, 5]
list_of_squares = []
for number in list_of_numbers:
    square = number **2
    list_of_squares.append(square) #Appends argument to the list in place
    print (f"The square of {number} is {square}, and our list of squares is now: {list_of_squares}")

#Iteration #, number, square, list_of_squares
#First iteration, 2, 4, [4]
#Second iteration, 3, 9, [4, 9]
#Third iteration, 4, 16 [4, 9, 16]
#Fifth iteration, 5, 25 [4, 9, 16, 25]

#Here is 2 other for loops for practice:
#Let's write a full loop that can calculate the sum of all numbers in the list
numbers_to_sum = [4, 8, 15, 16, 23, 42]
total = 0
for number in numbers_to_sum:
    total = total + number
    print(f"The current number is {number}. The updated total is {total}")
    print(total)
#How do we know if we have the right total?
print(total == sum(numbers_to_sum))

#Let's do the same thing for getting the maximum value in a list:
numbers = [-3, 5, 7, -12, 9, 31]

from math import inf
maximum = -inf
for x in numbers:
    if(x > maximum):
        maximum = x
    print(f"The current item is {x}. The new maximum is {maximum}")
print(maximum == max{numbers})