# exception = events detected during execution that interrupt the flow of a program

try:
    
    numerator = int(input("Enter a number to divide:"))
    denominator = int(input("Enter a number to divide by:"))

    result = numerator / denominator

except ZeroDivisionError as e:
    print("You can't divide by zero! idiot")
    print(e)

except ValueError as e:
    print(e)
    print("Enter only number pls")

except Exception as e:
    print(e)
    print("Something went wrong")

else:
    print(result)

finally:
    print("This will always execute")