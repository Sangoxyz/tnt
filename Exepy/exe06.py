""" 
Viết chương trình Python để tìm nghiệm của phương trình bậc hai ax^2 + bx + c. Biết rằng:

Nếu a và b cùng bằng 0 thì phương trình vô nghiệm
Nếu a = 0 thì phương trình có 1 nghiệm là (-c/b)
Nếu b^2-4ac < 0 thì phương trình vô nghiệm
Nếu a > 0 thì phương trình có 2 nghiệm phân biệt
dùng công thức tính.

"""
""" a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: ")) """


from cmath import sqrt  # thu vien
a, b, c = map(float, input().split())  # Nhap vao nhieu so

if a == 0:
    if b == 0:
        if c == 0:
            print("Pt vo so nghiem")
        else:
            print("Pt vo nghiem")
    else:
        print(f"Pt co nghiem duy nhat:{-c/b} ")
else:
    delta = b ** 2 - 4*a*c
    if delta > 0:
        x1 = (-b + sqrt(delta)) / (2*a)
        x2 = (-b - sqrt(delta)) / (2*a)
        print(x1, x2)
    elif delta == 0:
        x = -b / (2*a)
        print(x)
    else:
        print("Pt vo nghiem")

        



