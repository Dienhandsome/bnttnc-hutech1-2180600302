def tinh_tong_so_nguyen_duong_am(chuoi):
    tong_duong = 0
    tong_am = 0
    
    # Tách các số trong chuỗi
    so = ''
    for ky_tu in chuoi:
        if ky_tu.isdigit() or (ky_tu.startswith('-') and so == ''):
            so += ky_tu
        else:
            if so != '':
                so_int = int(so)
                if so_int > 0:
                    tong_duong += so_int
                elif so_int < 0:
                    tong_am += so_int
                so = ''
    
    # Xử lý số cuối cùng trong chuỗi
    if so != '':
        so_int = int(so)
        if so_int > 0:
            tong_duong += so_int
        elif so_int < 0:
            tong_am += so_int
    
    return tong_duong, tong_am

# Chuỗi đầu vào
chuoi = "-100# Asdfkj8902w3ir021@swf-20"

# Tính tổng
tong_duong, tong_am = tinh_tong_so_nguyen_duong_am(chuoi)

# In kết quả
print("Kết quả:")
print("Giá trị dương:", tong_duong)
print("Giá trị âm:", tong_am)