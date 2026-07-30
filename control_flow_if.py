#We are going to talk about control flow.
#Control flow is instrucctions that determine when, whether, and how often a section of code is going to run

my_name = "Katherine"
my_gender = "Female" 

if my_gender =='Female':
    print("Hello Ms. " + my_name)
elif my_gender == 'Male':
    print('Hello Mr.' + my_name)
elif my_gender =='Non-Binary':
    print("Hello" + my_name)
else:
    print("Hello" + my_name + ", how should I address you?")
#Anatomy of an If statement. 
#An if statement begins with if
#After if statement, there is a logical statement or logical test
#logical expression is any expression that evaluates to true or false
#after that, a colon:
#On the next line, follows an indented code block:
#Intended code block is what machine runs if logical statement evaluates to true. Otherwise it wont run

#After this code block you can have between zero and many elif statements
#Structure: elif LOGICAL_STATEMENT:
#each followed by their own code block: when will these code blocks run?
#1. When the logical statement is true and 2. None of the previous ones were true
#Conditional logic blocks run sequentially, one statement at a time
#Thet stop at the first true statement they encounter
#The final statement can be (but doesn't have to be ELSE)
#Else block will run when ALL statements are evaluated as False

#Very common GOTCHA with conditional statements:

def status_checker(age):
    if age >= 13:
        print("You are a teenager")
    elif age >= 18:
        print("You are an adult")
    elif age >=4:
        print("You are a kid")
    else:
        print("You are a baby")

status_checker(1)
status_checker(5)
status_checker(17)
status_checker(39)

#Correct status checker
def status_checker(age):
    if age >= 18:
        print("You are an adult")
    if age >= 13:
        print("You are a teenager")
    elif age >=4:
        print("You are a kid")
    else:
        print("You are a baby")
#Always check the most restrictive condition first (18 with adult needs to go first) or else function assumes 
#any age over 13 is a teenager

def can_legally_drink(country,age):
    if (country == "USA"):
        if (age >= 21):
            return True
        else:
            return False
    elif (country == "Canada"):
        if (age >= 19):
            return True
        else:
            return False
    elif (country == "Germany"):
        if (age >= 16):
            return True
        else:
            return False
    else:
        return "Dont know"

#Trick #1: You can write a simple if statement in one line.
#This is allowed, its called the "Ternary operator":
age = 22
status = "Adult" if age >= 18 else "Minor"
#Value_if_true if logical_statement else valie_if_false
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

#Trick #2: You can sometimes save additional effort if using a dictionary rather than an if statement.

#Let's say you want to map countries to their currency

def get_country_currency(country):
    if country == "USA"
        return "US Dollars"
    elif country == "Canada"
        return "Canadian Dollars"
    elif country == "France"
        return "Euros"
    elif country == "Japan"
        return "Yen"
    else:
        return "Country not found"
#Good but not great
#We always check the value of one variable (country) and depending on the value, we return another value

#This works a lot like a dictionary
country_currency = {
    "USA": "US Dollars",
    "Canada": "Canadian Dollars"
    "France": "Euros"
    "Japan": "Yen"}
#How do we get the currency?
country_currency["France"]

#This not the same thing
get_country_currency("Iran") #Country not found:
country_currency["Iran"] #KeyError

#However...
country_currency.get("Iran", "Country not found")
