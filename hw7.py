shopping_bag = {}
print('[구입]')
while True:
    item = input('상품명? ')
    if item == '' or item == ' ':
        break
    else :
        much = int(input('수량은? '))
        shopping_bag[item] = much
        print(f'장바구니에 {item} {much}개가 담겼습니다.\n')

print(f'\n>>> 장바구니 보기:{shopping_bag}')

check_item = input('장바구니에서 확인하고자 하는 상품은? ')
if check_item in shopping_bag:
    num = shopping_bag.get(check_item)
    print(f'{check_item}은(는) {num}개 담겨 있습니다.')
