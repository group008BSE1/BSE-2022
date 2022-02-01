try:
    location = input('Location: ').lower()
    pay = int(input('Pay: '))
    decision_1 = "Without a doubt,I'll take it"
    decision_2 = "No Thanks, I can find something better"
    decision_3 = "No way!"
    decision_4 = "Sure, I can work with this"
    if location == 'mbarara':
        if pay < 4000000:
            print(decision_3)
        elif pay == 4000000:
            print(decision_2)
        elif pay > 4000000:
            print(decision_1)
    elif location == 'kampala':
        if pay < 10000000:
            print(decision_3)
        elif pay ==10000000:
            print(decision_4)
        elif pay > 10000000:
            print(decision_1)
    elif location == 'space':
        print(decision_1)
    else:
        if pay < 6000000:
            print(decision_2)
        elif pay >= 6000000:
            print(decision_4)
except:
    print('Wrong Input')