def solution(number):
    a=[]
    for b in range(number):
        if b % 3 == 0 or b % 5 == 0:
            a.append(b)
    return sum(a)