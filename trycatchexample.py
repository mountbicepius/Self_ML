def exampleTry():
  num = int(input('Enter a number\t'))
  value =None
  try:
    value = 100 / num
    print(f'Your answer is {value}')
  except:
    print('Cannot divide by zero')
  finally:
    print(value)

if __name__=="__main__":
  exampleTry()