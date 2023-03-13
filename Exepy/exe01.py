""" 
Viết một phương trình Python để nhập lương nhân viên, tính thuế thu nhập và lương cơ
 bản (số  tiền lương thực sự mà nhân viên đó nhận được). Với các thông số giả sử như
 sau (không theo luật lương, chỉ là con số giả sử để dễ tính toán):

 30% thuế thu nhập nếu lương là 15 triệu
 20% thuế thu nhập nếu lương từ 7 đến 15 triệu.
 10% thuế thu nhập nếu lương dưới 7 triệu
 """

""" 
input: Lương nhân viên
output:
- Thuế thu nhập
- Lương cơ bản
logic: 
- nếu lương < 7 thì thuế thu nhập = 0.1 * lương và lương thực nhận = lương * 0.9
- ngược lại nếu lương < 15 thì thuế thu nhập = 0.2 * lương và lương thực nhận = lương * 0.8
- Còn lại thuế thu nhập = 0.3 * lương và lương thực nhận = lương * 0.7
"""
luong = int(input("Nhap luong nhan vien: "))

if luong < 7:
    print("Thue thu nhap:", 0.1 * luong)
    print("Luong thuc nhan:", 0.9 * luong)
elif luong < 15:
    print("Thue thu nhap:", 0.2 * luong)
    print("Luong thuc nhan:", 0.8 * luong)
else:
    print("Thue thu nhap:", 0.3 * luong)
    print("Luong thuc nhan:", 0.7 * luong)
