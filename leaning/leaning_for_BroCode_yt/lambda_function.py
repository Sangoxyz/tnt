# lambda function = function written in 1 line using lambda keyword
#                   acccepts any number of arguments, but only has one expression
#                   (thing of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
# lambda parameters:expression

""" def double(x):
    return x * 2

print(double(5)) """

double = lambda x : x * 2
multiply = lambda x, y : x * y
add = lambda x, y, z : x + y + z
full_name = lambda fist_name, last_name : fist_name + " " + last_name
age_check = lambda age : True if age >= 18 else False

print(age_check(17))
print(full_name("Sang","code"))
print(add(5, 6, 7))
print(multiply(5, 6))
print(double(5))