file_name = input("Enter file name: ")
try:
    open_file = open(file_name,'r')
    count = 0
    for line in open_file:
        count += 1
    print(f'There were {count} subject lines in {file_name}')
except:
    if file_name == "na na boo boo":
        print(f"{file_name.upper()} - You have been punk'd")
    else:
        print(f"File cannot be opened: {file_name}")



