# functions

print("Hello world")

# difining the function
def greet():
  print("Hello")

print("Hey there")

# calling or executign the function
greet()

# functions with arguments
# num1 and num2 are parameters of the functions => variables of the function
# the values 7 and 9 are called arguments
# number of arguments = number of parameters
# arguments must follow the order of the parameters

# position parameters/arguments
def add_nums(num1, num2):
  print(num1 + num2)

add_nums(7, 9)
add_nums(15, 75)
add_nums(8, 56)

def full_name(f_name, l_name):
  print(f"{f_name} {l_name}")

full_name("Hrithik", "Roshan")
full_name("Kumar", "Akshay")

# functions with keyword arguments
full_name(l_name="Kumar", f_name="Akshay")

# functions with default arguments
def greeting(greet_word, name="Annonymous"):
  print(f"{greet_word} {name}")

greeting("Hello", "Haashim")
greeting("Hi", "Dinesh")
greeting("Good morning")
greeting("What's up ")

# return statement
def sqareNum(num):
  return num**2 # the function exits here

result = sqareNum(9) # return the value of 81

if result == 81:
  print("The answer is correct")