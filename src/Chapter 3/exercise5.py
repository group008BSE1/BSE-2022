try:
    guests = int(input("Enter the number of guests: "))
    if guests > 0 and guests <= 50:
        cost = "$4000"
    elif guests > 50 and guests <= 100:
        cost = "$10000"
    elif guests > 100 and guests <= 200:
        cost = "$15000"
    elif guests > 200:
        cost = "$20,000"
    print("Your cost is:",cost)
except:
    print("Wrong input")
