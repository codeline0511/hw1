from Fixed_price import get_fixed_price as Fp

discount_much = int(input('할인율은?'))

A_discount_price = int(input('A 상품의 할인된 가격은?'))
result = Fp(discount_much, A_discount_price) 

B_discount_price = int(input('B 상품의 할인된 가격은?'))
result_1 = Fp(discount_much, B_discount_price)

print('A 상품의 정가는', result, '원')
print('B 상품의 정가는', result_1, '원')

