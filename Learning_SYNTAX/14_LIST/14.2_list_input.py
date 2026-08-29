raw_data = input("Enter items for list seperated by comma (',') : ")
print(raw_data)

list_data = [item.strip() for item in raw_data.split(",")]
print(list_data)