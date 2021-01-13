from itertools import count

for el in count(int(input('Enter starting number '))):
    if el > 100:
        break
    else:
     print(el)
# itertools.count(start=0, step=1) - бесконечная арифметическая прогрессия с первым членом start и шагом step.

from itertools import cycle
count = 1
myList = input('Enter elements of list by a space: ').split()
for el in cycle(myList):
    if count >10:
        break
    print(el)
    count+=1
# itertools.cycle(iterable) - возвращает по одному значению из последовательности, повторенной бесконечное число раз.