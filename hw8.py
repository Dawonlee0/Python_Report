# 개념 확인 과제(10.6)
shopping_bag = {}

def buy():
    print('[구입]')
    while 1:
        a = input('상품명? : ')
        b = input('수량은? : ')
        if a == '':
            break
        else:
            shopping_bag[f'{a}'] = b
            print(f'장바구니에 {a}가 {b}개 담겼습니다')
    print(f'장바구니 보기 : {shopping_bag}')

    return shopping_bag

def serch(shopping_bag):
    print('[검색]')
    find = input('장바구니에서 확인하고자 하는 상품은? : ')
    if find in shopping_bag:
        print(f'{find}는 {shopping_bag.get(find, "해당 상품이 없습니다.")}개 있습니다.')
    else:
        print(f'장바구니에 {find}은(는) 없습니다')

def show(shopping_bag):
    print(f'장바구니 보기 : {shopping_bag}')

# 주 프로그램 부
shopping_bag = buy()
show(shopping_bag)
serch(shopping_bag)
