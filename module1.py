
def sal():
     try:
          time = float(input('Enter working time '))
          salary = float(input('Enter salary in dollars '))
          premium = float(input('Enter the premium to the salary in dollars '))
          result = time * salary + premium
          return result
          # print(f'salary for an emplotee: {result} $')
     except ValueError:
          print('Not a number')
     print("The largest purchase was ${}.".format(round(result, 2)))