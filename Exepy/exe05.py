""" 
Viết phương trình Python xếp hạng học lực của học sinh dược trên các điểm bài kiểm tra, điểm thi giữa kỳ, điểm thi cuối kỳ, Nếu:

Điểm trung bình >= 9.0 là hạng A
Điểm trung bình >= 7.0 và < 9.0 là hạng B
Điểm trung bình >= 5.0 và < 7.0 là hạng c
Điểm trung bình < 5.0 là hạng F
"""
dkt = float(input("Nhap diem kiem tra: "))
dtgk = float(input("Nhap diem thi giua ky: "))
dtck = float(input("Nhap diem thi cuoi ky: "))

dtb = (dkt + dtgk + dtck) / 3

if dtb < 5:
    print("Hang F")
elif dtb < 7:
    print("hang C")
elif dtb < 9:
    print("hang B")
else:
    print("hang A")


