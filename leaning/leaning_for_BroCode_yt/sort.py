# sort() method = used with lists



""" students = ['Squidward', 'Sandy', 'Patrick', "Spongebob", 'Mr. Krabs']

students.sort(reverse=True)

for i in students:
    print(i) """

# sort() function = used with iterables

""" students = ('Squidward', 'Sandy', 'Patrick', "Spongebob", 'Mr. Krabs')
sorted_students = sorted(students,reverse=True)

for i in sorted_students:
    print(i) """

# sort() method = used with lists 

""" students = [('Squidward', "F", 60), 
            ('Sandy', "A", 33), 
            ('Patrick', "D", 36), 
            ("Spongebob", "B", 20), 
            ('Mr. Krabs', "C", 78)]
grade = lambda grades : grades[1]           # sap xep A - Z
students.sort(key=grade, reverse=False)     # sap xep A- Z

for i in students:
    print(i)


age = lambda ages : ages[2]
students.sort(key=age,reverse=False)

for i in students:
    print(i) """

# sort() function = used with iterables <tuple>

students = (('Squidward', "F", 60), 
            ('Sandy', "A", 33), 
            ('Patrick', "D", 36), 
            ("Spongebob", "B", 20), 
            ('Mr. Krabs', "C", 78))

age = lambda ages : ages[1]           # sap xep A - Z
sorted_students = sorted(students, key= age)    # sap xep A- Z
for i in sorted_students:
    print(i)
