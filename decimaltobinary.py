def toBinary(num):
  if num >=1:
    toBinary(num//2)
    print(num % 2)
  
if __name__ == '__main__':
  toBinary(int(input('enter a decimal\t')))