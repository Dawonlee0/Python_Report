# 개념 확인 과제 5.5

# 할인 전 가격 계산 함수
def get_fixed_price(sale, A1, B2):
    sale1 = sale * 0.01
    A11 = A1 / (1-sale1)
    B22 = B2 / (1-sale1)

    print('상품의 정가는', int(A11), '원')
    print('상품의 정가는', int(B22), '원')


# 할인율, A, B 상품 가격 입력
sale = int(input('할인율은? : '))
A1 = int(input('A 상품의 할인된 가격은? : '))
B2 = int(input('B 상품의 할인된 가격은? : '))

# 함수실행
get_fixed_price(sale, A1, B2)
