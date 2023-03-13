""" Viết chương trình Python kiểm tra số nguyên nhập vào là
- số dương chẵn
- số dương lẻ
- số âm chẵn
- số âm lẻ """


num = int(input("Nhap vao so nguyen: "))

if num == 0:
    print("So khong")
else:
    s = 'duong'

    if num < 0:
        s = 'am'

    s1 = 'chan'
    if num % 2 != 0:
        s1 = 'le'

    print(f"So {s} {s1}")



