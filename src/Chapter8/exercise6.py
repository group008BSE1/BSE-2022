number_list = []
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
        try:
            number_list.ap pend(int(num))
        except:
            print("Enter a valid number")
print(f"The minimum number is {min(number_list)}")
print(f"The maximum number is {max(number_list)}")
