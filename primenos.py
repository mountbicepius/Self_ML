def isPrime():
  num1 = int(input('Enter the start of interval\t'))
  num2 = int(input('Enter the ending of the interval\t'))
  for num in range(num1,num2+1):
    # all prime numbers are greater than 1
    if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

if __name__ == "__main__":
  isPrime()
  