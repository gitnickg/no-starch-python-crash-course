### = explaination
# = commented code

##### Resources
##### https://ehmatthes.github.io/pcc_3e/
##### https://github.com/ehmatthes/pcc_3e/

#import this

######################
##### CHAPTER 01 #####
######################

### prints Hello python!
#print ("Hello python!")

######################
##### CHAPTER 02 #####
######################

### stores a string in a variable and prints the variable
#message = "hello no starch!"
#print (message)

### mistakes
#error_message = "this will not print"
#print (Error_message)

### variables and methods
#name = "john wick"
#print (name.title())
#print (name.upper())
#print (name.lower())

#first_name = "john"
#last_name = "wick"
#full_name = f"{first_name.title()} {last_name.title()}"
#print(full_name)

### formatting

#print("\tthis is tabbed")

#print("this \nis \na \nnew \nline")

### remove whitespace r_strip() l_strip() strip()
#white_space = "this sentence has trailing white space   "
#print(white_space.rstrip())

### removing a prefix
#nostarch_url = "https://nostarch.com"
#nostarch_url = nostarch_url.removeprefix("https://")
#print(nostarch_url)

### syntax error, cannot use same quotes for string and grammer '' vs ""
#message = 'one of python's strengths is it's cool and whatnot'
#print(message)


### Numbers
#2 + 2 add
#3 - 2 subtract
#2 * 2 multiply
#3 / 2 divide
#3 ** 2 exponents
#(2 + 3) * 4 BEDMAS
#0.1 + 0.1 floats

### make numbers more readable with _
#universe_age = 14_000_000_000

### multiple variable assignment
#x, y, z = 0, 0, 0

### Constant variable with uppercase
#MAX_CONNECTIONS = 5000

######################
##### CHAPTER 03 #####
######################

### lists
#names = ['bob', 'alice', 'john']
#print(names[0].title())

### prints the last item in the list
#print(names[-1])

### change a list item
#names[0] = Steve

### adding to the list
#names.append('billy')

### insert an item into a list
#names.insert(0, 'jimmy')

### remove an item from a list
#del names[0]

### removing an item from a list and storing it as a variable, pop() for last item
#removed_name = names.pop(0)

### removing a specific item value
#names.remove('jimmy')

### sorting
#list.sort()
#sorted(list)

### length
#len(list)







