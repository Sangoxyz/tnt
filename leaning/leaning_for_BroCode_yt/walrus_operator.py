# walrus operator := 

# assignment experssion aka walrus operator
# assignment values to variables as part of a larger a larger expression

""" foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food) """

foods = list()

while food := input("What food do you like?: ") != "quit":
    foods.append(food)