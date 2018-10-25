def validate_pin(pin):
    try:
        if len(pin) != 4 and len(pin) != 6 or list(map(int, pin)):
            return False
        return True
    except:
        return False

print(validate_pin('-00000'))

"Best solutions":

def validate_pin2(pin):
    return len(pin) in (4, 6) and pin.isdigit()

import re
def validate_pin3(pin):
    return bool(re.match(r'^(\d{4}|\d{6})$',pin))