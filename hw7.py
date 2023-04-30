# 개념과제
shopping_bag = {}

print('[구입]')
while 1:
    a = input('상품명? : ')
    b = input('수량은? : ')

    if a == ' ':
        break
    else:
        shopping_bag[f'{a}'] = b
        print(f'장바구니에 {a}가 {b}개 담겼습니다')

print(f'장바구니 보기 : {shopping_bag}')
print('[검색]')

find = input('장바구니에서 확인하고자 하는 상품은? : ')
print(f'{find}는 {shopping_bag.get(find, "해당 상품이 없습니다.")}개 있습니다.')
