# for in loop
country = "Philippines"
for letter in country:
  print(letter)

country1 = "Hong Kong"
for char in country1:
  print(char)

# range loop
# default initial value of i is 0
# default increment is 1
for i in range(10):# (initial value of i, final value of i, increment in i)
  print(i)

fruit = "Watermelon"
print(len(fruit))
print(fruit[0])
print(fruit[1])
for i in range(len(fruit)):
  print(fruit[i])

# while loop
i = 0
while(i < len(fruit)):
  print(fruit[i])
  i+=1 # i = i + 1

x = 100
while(x <= 200):
  print(x)
  x+=10

# infinite loops with while loop
y = 10
while(y < 20):
  print(y)
  y+=2

# nested loops
colors = ["red", "blue", "green"]
fruits = ["apple", "banana", "cherry"]

for x in colors:
    for y in fruits:
        print(x, y)