worked_hours = int(input('Enter Hours: '))
rate = float(input('Enter rate: '))
normal_hours = 40
worked_pay = worked_hours*rate
#bonus_pay
if worked_hours>normal_hours:
    extra_hours = worked_hours-normal_hours
    extra_pay = extra_hours * rate * 1.5
    normal_hours_pay = normal_hours * rate
    final_pay = normal_hours_pay + extra_pay
    print('Pay:',final_pay)
else:
    print('Pay:',worked_pay)



