""" Viết phương trình Python kiểm tra một năm nhập vào có phải năm nhuận hay không? """



nam = int(input("Nhap vao nam: "))

if(nam % 400 ==0) or (nam % 4 ==0 and nam % 100 != 0):
    print(nam, "la nam nhuan")
else:
    print(nam, "khong phai nam nhuan")
    