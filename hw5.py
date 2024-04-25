def read_number(a):
    n1 = a // 100
    ex_1 = a % 100
    n2 = ex_1 // 10 
    n3 = ex_1 % 10

    L1 = read_single_digit(n1)
    L2 = read_single_digit(n2)
    L3 = read_single_digit(n3)

    a_1 = (f'{L1} {L2} {L3}')
    return a_1

def read_single_digit(n):
    if n == 0:
        return '영'
    elif n == 1:
        return '일'
    elif n == 2:
        return '이'
    elif n == 3:
        return '삼'
    elif n == 4:
        return '사'
    elif n == 5:
        return '오'
    elif n == 6:
        return '육'
    elif n == 7:
        return '칠'
    elif n == 8:
        return '팔'
    else:
        return '구'

num = input("세 자리 정수 입력: ")
print(f'{read_number(num)}')
