""" 
Viết chương trình Python để người dùng nhập vào 3 số nguyên và tìm số lớn nhất trong 3 số đó
"""
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

max_ab = a

if b > a:
    max_ab = b

max_abc = c

if max_abc < max_ab:
    max_abc = max_ab
print(f"So lon nhat la {max_abc}")
