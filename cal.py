data_list = []
print("Enter data (type '.' to exit): ")
data_str = input()

while data_str != '.':
    swap_data = data_str[::-1]  # กลับด้านของสตริง

    data_int = int(data_str)
    swap_data_int = int(swap_data)

    data_list.append(data_int)
    data_list.append(swap_data_int)

    print("Enter data (type '.' to exit): ")
    data_str = input()

# แสดงผลลัพธ์
print("Result:", end=" ")
for item in data_list:
    print(item, end=" ")
