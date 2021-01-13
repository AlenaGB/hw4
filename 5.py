from functools import reduce

def multiply(el1, el):
     return el1 * el
print(f'list of even values {[el for el in range(100, 1000) if el % 2 == 0]}')
print(f'result of multiplication {reduce(multiply, [el for el in range(100, 1000) if el % 2 == 0])}')