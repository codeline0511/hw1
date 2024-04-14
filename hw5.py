def read_single_digit(n):
    if n == '0':
        return '영'
    elif n == '1':
        return '일'
    elif n == '2':
        return '이'
    elif n == '3':
        return '삼'
    elif n == '4':
        return '사'
    elif n == '5':
        return '오'
    elif n == '6':
        return '육'
    elif n == '7':
        return '칠'
    elif n == '8':
        return '팔'
    elif n == '9':
        return '구'

def read_number(a):
    a_1 = a[0]
    a_2 = a[1]
    a_3 = a[2]
    digit_1 = read_single_digit(a_1)
    digit_2 = read_single_digit(a_2)
    digit_3 = read_single_digit(a_3)
    digit = digit_1, digit_2, digit_3
    return digit


num = input("세 자리 정수 입력: ")
print(f'{read_number(num)}')
