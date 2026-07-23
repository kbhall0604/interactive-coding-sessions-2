#Talk about collections:
#Collections are different ways of storing things into a single variable.
#Prior to this only one thing was assigned to one variable:
a = "hello"
b = 3.14

#Now we learn how to assign multiple things to a single variable: collection
#There are 2 we will cover. The first being LISTS

my_empty_list = [] #Two square brackets
#This is a list:
type(my_empty_list) # New type of object! int, str, float, bool, decimal, list

# LISTS are ordered collections of items
# You can use it to store a sequence of other elements:

my_favorite_numbers = [1, 2, 3, 4, 5,] #separate items in a list by commas
# Lists can also contain strings:
my_favorite_colors = ['red', 'blue', 'white']
#floats too
my_favorite_floats = [3.14,  2.718, 1.618]
my_favorite_bools = [False, True, False]
#Note that lists can contain repeated elements. They dont need to be unique
#You can also put different things in a list:
my_mixed_list = [False, 3.14, "Katherine", 1, True]
#You can put lists inside a list
my_list_of_lists = [[1, 2], ["hello", 2], [False, 3.14]]
#Anything can go inside of lists
#A list is an object, meaning lists have methods
#See what exists inside of lists:
my_favorite-colors #we can print this to see what's inside
my_favorite_colors.append #Append is a method used for adding element(s) to a list
print(my_favorite_colors.append("purple"))
#When you run append on a list, nothing is returned.
#This is different than what happens when you run a method on a strong. A transformtation
#of the string is returned
my_name = "Katherine"
print(my_name.upper())

#We ran a methods on the list my_favorite_colors and got nothing in return. Why?
print(my_favorite_colors)

print(my_name) #This remains lowercase because when we run a method on a string, a
#new string is returned. It does not modify, or mutate, the original

#With the list we saw a mutation: After we ran append(), it changed the original
#content of the list, but it did not return anything. It changed the orginal list

my_favorite_colors.append('purple')
print(my_favorite_colors)
#Everytime you run append, additional content is added to the list

#Lists are MUTABLE, meaning their methods modify them directly. They do not
#return a copy of the list. They change the content of the list.

#Let's learn another method on lists:
a = my_favorite_colors.pop() #Removes last item of list and returns it
print(my_favorite_colors)
print(a)
#Now we know pop() removes last item of list and returns it and append adds an item

#Because they are ordered, we can check what is located at a given position in
#the list. This is called INDEXING.

my_favorite_numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
#To get the elements located at a given INDEX in the list
#We can use [1], where 1 is the index of the element we want to get

print(my_favorite_numbers[0])

#How would I get the 4th element of the lsit
print(my_favorite_numbers[3])

#How would I get the 6th element?
print(my_favorite_numbers[12]) #Index error- because this list is shorter than that

#How would I get the last element?
#Determine how many elements are in the list:
n_numbers = len(my_favorite_numbers) #len is a function that tells you how many 
#items are in a list
my_favorite_numbers[n_numbers - 1]
#There is an easier way to achieve the same thing:
my_favorite_numbers[-1]
my_favorite_numbers[-2] #This counts from the second to last

#Thats called indexing: how we can grab a single element from the list.
#Now, how can we grab multiple elements from a list
#We can use something called slicing formatted -> my_list[start:stop:step]
#star explains where to start in list, stop tells you where we stop, step explains 
#how many items we are skipping
#Here are some examples:
my_favorite_numbers[0:5:1] #This grabs all the elements between index 0 and 5
#(exculsive), not skipping any
my_favorite_numbers[1:4:1] #Grab all elements between 1 and 4 
my_favorite_numbers[0:6:2] #All numbers between 0-6 skipping every other (2)
#you can ommit some of these arguments when slicing: 
my_favorite_numbers[0:5] #What is omitted? Step -> giving 1-4. When step is 
#omitted python assumes 1 is in there
my_favorite_numbers[:6:1] #Now start is omitted which defaults to 0
my_favorite_numbers[::1] #Now start and stop are omitted. Stop defaults to the 
#length of the list
my_favorite_numbers[::] #Now nothing is specified which causes the full list
#to be generated

my_favorite_cities = ["Boulder", "Paris"]
katherine_favorite_cities = my_favorite_cities 
print(my_favorite_cities)
print(katherine_favorite_cities)
my_favorite_cities.append('Barcelona')
print(my_favorite_cities)
katherine_favorite_cities.append('Milan')
print(katherine_favorite_cities)
print(my_favorite_cities)
#By writing this I say my favorite cities and katherine favorite cities
#are defined by the same list

my_favorite_cities = ["Boulder", "Paris"]
katherine_favorite_cities = my_favorite_cities[::] #Creates a copy of the list
#or you can do my_favorite_cities.copy()
print(my_favorite_cities)
print(katherine_favorite_cities)
my_favorite_cities.append('Barcelona')
print(my_favorite_cities)
katherine_favorite_cities.append('Milan')
print(katherine_favorite_cities)
print(my_favorite_cities)

my_name = "Katherine"
print(my_name[1:4]) #You can index and slice strings
#Anthing that is a collection and ordered can be indexed

#Since lists are mutable, you can do more than reading their content with index
#and slicing
my_favorite_colors # ['red', blue', 'white', 'purple']
#How would we switch blue to pink
#At index one:
my_favorite_colors[1]
my_favorite_colors[1] = "pink"
print(my_favorite_colors) #This allowed pink to replace blue in spot 1
#if you want to add something to the middle of the list, you can use insert
my_favorite_colors.insert(1, 'gold')
print(my_favorite_colors) #Now gold was inserted into position 1

#Lastly, we can swap multiple values at the same time.
my_favorite_colors[0:2] #We have a list of 2 elements that can be sswapped
#with 2 other elements
my_favorite_colors[0:2] = ['yellow', 'orange']
print(my_favorite_colors)
#Whar if the sequence length for substitution does not match the original length
my_favorite_colors[0:2] = ['black']
print(my_favorite_colors) #Here both red and gold in spots 1 and 2 are replaced 
#by just black (1 new variable). This is acceptable

my_name = "Katherine" 
my_name [0] = "X" #Strings are immutable
#you can read a sgtring with indexing and slicing but you cant write to it.

#Another type of collections are called Dictionaries (DICTS)
#A dictionary is a collection of key-value pairs
#There are key ('words') that have values ('definitions') much like a real dictionary

#Here's how to create a dictionary:
my_friends_age = {"Nick" : 40,
                  "Sam" : 35,
                  "Juan" : 37}
#Curly brackets, and inside  is indoe

#The values in a dictionary can be different:
my_information = {"name": "Katherine",
                  "age": 22,
                  "hobbies":["skiing", "crafting", "watching movies"]}
#These are typically str, but sometimes int
#They must be unique and immutable

#How to use:
#Once created, INDEX it with a key
#To know the value of that key:
my_friends_age["Nick"]
my_information['hobbies']
#Dictionaries, like lists, are mutable.
#Meaning we can reach into them and update a value associated with a key
my_friends_age["Nick"] = 41
my_friends_age
#How to add in another friend with their age
my_friends_age["Alice"] = 56
my_friends_age

#Dictionaries are also objects, meaning they have methods:
#Two usefule methods. 
#What do we do if we're unsure whether or not a dictionary has a value
#When we try to index with that key we may get an error
my_friends_age["Nico"] #This would cause an error
#We want to avoid errors since they stop code so we can use 'get()' instead
my_friends_age.get("Nico") #If the key exists a value is returned, if it doesn't
#None will be returned

#If you want to delete a key from a dictionary:
my_friends_age.pop('Sam') #Pop for a list takes a numerical index for a dict, it 
#takes a key
my_friends_age
#Three methods to see whats in a dictionary:
my_friends_age.keys() #Prints all the keys that exist:
my_friends_age.values() #Print all the values that exist:
my_friends_age.items() #Prints all the key-value pairs.

#Lastly it's important to note that values can be dictionaries themselves!
#This is a very common data structure to represent users:

my_friends_info = {
     # Master dict: keys are going to be user names
        #and the values are going to be dictionaties containing
        #Information about the users.
   "Nick":{
        "age": 41,
        "hobbies": ['basketball', 'cooking'],
        "city": "Boulder"
    },
    "Sam": {
        "age": 35,
        "hobbies": ['hiking', 'painting'],
        "city": "Chicago"
    }
}
#How to use a more complex structure like this?
#How to get all of Nick's info
my_friends_info["Nick"]
nicks_info = my_friends_info["Nick"]
print(type{nicks_info})
#So how can we get Nick's age from my_friends_info

print(my_friends_info['Nick']['age']) #Paranthesis can be used to make the order
#of things make more sense

#How could you look for your friend Sam's hobby information
print(my_friends_info.get('Sam')['hobbies'])

#What would happen if Sam doesn't exist?
my_friends_info.get('Lisa')['hobbies'] #This fails because Lisa does not exist
#in this dictionary

#Nick recently started sourdough baking. How can thus hobby be added
my_friends_info.append('Nick')['hobbies = basketball, cooking, sourdough baking'] #Fail
my_friends_info["Nick"]["hobbies"].append('sourdough baking') #Works!
print(my_friends_info)
#what about adding two hobbies at once?
my_friends_info["Nick"]["hobbies"].append('sourdough baking').ap
