
""" try:

    with open('test.txt') as file:
        print(file.read())

except FileNotFoundError:
    print('That file was not found')
 """

text = "Have a nice day! See ya"

with open('test.txt','w') as file:
    file.write(text)