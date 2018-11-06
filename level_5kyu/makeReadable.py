def make_readable3(seconds): # Using F string TO USE From python 3.6
    return f'{seconds//3600:02}:{(seconds % 3600)//60:02}:{seconds%60:02}'

def make_readable1(seconds): # Using .format
    return '{:02}:{:02}:{:02}'.format(seconds//3600, seconds%3600//60, seconds%60)

def make_readable(seconds): # Using percentage format
    return "%02d:%02d:%02d" % (seconds//3600, seconds%3600//60, seconds%60)


print(make_readable(62))
print(make_readable(35999))