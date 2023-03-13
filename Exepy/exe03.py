""" 
Viết chương trình Python để nhập một số nguyên bất kỳ từ bàn phím và in kết quả ra màn hình để thông báo cho người dùng biết số đó lớn hay nhỏ hơn 100
"""
number = int(input("Nhap vao so nguyen: "))

if number > 100:
    print("So vua nhap lon hon 100")
elif number < 100:
    print("So vua nhap nho hon 100")
    

