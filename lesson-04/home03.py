for i in range(1,101):
    d = 1
    print(d)
    should_break = input('Should we break?').lower()
    while should_break == 'no':
        d+=i
        print(d)
        should_break = input('Should we break? ').lower()
        while should_break != 'yes' and should_break != 'no':
            print("Don't understand you")
            should_break = input('Should we break? ').lower()
    else:
         break