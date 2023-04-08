# 개념 확인 과제 7.6

def read_single_digit(num):
    number = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    return number[num]

def read_number(n):
    n0 = read_single_digit(int(n[0]))
    n1 = read_single_digit(int(n[1]))
    n2 = read_single_digit(int(n[2]))
    return n0 + " " + n1 + " " + n2

n = input('세 자리 정수 입력: ')
n123 = read_number(n)
print(n123)
