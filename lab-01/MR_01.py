



def hoan_vi(lst, start, end):
    if start == end:
        print(lst)
    else:
        for i in range(start, end + 1):
            # Hoán vị phần tử thứ start với các phần tử sau nó
            lst[start], lst[i] = lst[i], lst[start]
            # Gọi đệ quy để hoán vị phần tử tiếp theo
            hoan_vi(lst, start + 1, end)
            # Đảo lại để trở về trạng thái ban đầu
            lst[start], lst[i] = lst[i], lst[start]

# Danh sách ban đầu
danh_sach = [1, 2, 3]

# In tất cả các hoán vị
hoan_vi(danh_sach, 0, len(danh_sach) - 1)