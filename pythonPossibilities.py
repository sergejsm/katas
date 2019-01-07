import math

sqrootL = lambda x, y: math.sqrt(x) + y



def greet(action):
    def say_hello():
        print(f'You, you be cool')

    def congratulate():
        print(f'Congrats')

    if action == True:
        return say_hello
    else:
        return congratulate

