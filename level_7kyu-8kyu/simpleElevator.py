def goto(level,button):
    if level in [0,1,2,3] and button in ['0','1','2','3']:
        return int(button) - level
    else:
        return '0'

print(goto('0','1'))