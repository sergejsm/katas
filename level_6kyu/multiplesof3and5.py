def solution(number):
    return sum([mult for mult in range(number) if mult % 3 == 0 or mult % 5 ==0])



print(solution(10))