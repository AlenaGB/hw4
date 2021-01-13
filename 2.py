myList = input('Enter numbers by a space: ').split()
newList = [el for num, el in enumerate(myList) if myList[num - 1] < myList[num]]
print(f'The original list {myList}')
print(' '.join(newList))
