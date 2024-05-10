def buy(l):
    while True:
        print('[구입]')
        item = input('상품명? ')

        if item == '':
            print()
            return False
        else:
            num = int(input('수량은? '))
            l[item] = num
            print(f'장바구니에 {item} {num}개가 담겼습니다.\n')
            

def show(lst):
    print(f'>>> 장바구니 보기: {lst}')

def find(key):
    print('\n[검색]')
    s = input('장바구니에서 확인하고자 하는 상품은? ')
    get_key = key.get(s)
    if s in key:
        print(f'{s}은(는) {get_key}개 담겨 있습니다.')
    else:
        print(f'장바구니에 {s}은(는) 없습니다.')                            

shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)
