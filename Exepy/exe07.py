""" 
Cửa hàng của bạn nhận gửi bán sản phẩm cho một công ty khác và hưởng hoa hồng theo doanh số bán như sau:

5% nếu tổng doanh số nhỏ hơn hoặc bằng 100 triệu
10% nếu tổng doanh số nhỏ hơn hoặc bằng 300 triệu
20% nếu tổng doanh số là lớn hơn 300 triệu.
Hãy viết phương trình Python để tính hoa hồng bạn sẽ nhận được dựa trên doanh số bán hàng
"""
dsbh = int(input("Nhap doanh so ban hang: "))

if dsbh <= 100:
    print("Hoa hong: ", (5/100) * dsbh)
elif dsbh <= 300:
    print("Hoa hong: ", (10/100) * dsbh)
else:
    print("Hoa hong: ", (20/100) * dsbh)
