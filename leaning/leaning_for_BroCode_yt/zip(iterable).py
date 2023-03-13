# zip(*iterable) = aggregate elements from two or more iterable (list, tuples, sets, etc)
#                  creates a zip object with paired elements stored in tuples for each elements

usenames = ("Xuan", "Bro", "Sang")
passwords = ("p@ssword", "abc123", "guest")

users = dict(zip(usenames, passwords))

print(type(users))

for key, value in users.items():
    print(key+ " : " + value)

# -----------------------------------------------------
usenames = ["Xuan", "Bro", "Sang"]
passwords = ["p@ssword", "abc123", "guest"]

users = (zip(usenames, passwords))

print(type(users))


for i in users:
    print(i)

