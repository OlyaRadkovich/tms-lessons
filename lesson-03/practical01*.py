s = input('Enter any number of seconds')
days = int(s) // (60**2*24)
hours = (int(s) - int(days)*60**2*24) //60**2
minutes = (int(s) - int(days)*60**2*24 - int(hours)*60**2) // 60
seconds = int(s) % 60
print('It turns out ' + str(days) + ':' + str(hours) + ':' + str(minutes) + ':' + str(seconds))
