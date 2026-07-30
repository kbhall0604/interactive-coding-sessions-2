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