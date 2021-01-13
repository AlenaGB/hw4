myList = input('Enter numbers by a space: ').split()
newList = [el for el in myList if myList.count(el) == 1]
print(' '.join(newList))