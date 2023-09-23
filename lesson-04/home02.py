for i in range(1,101):
    d = 1
    print(d)
    should_break = input("Should we break? Enter 'yes' or 'no' ")
    while should_break == 'no':
        d+=i
        print(d)
        should_break = input('Should we break? ')
    else:
         break
