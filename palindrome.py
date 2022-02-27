import math
  
def palindrome(num):
    return int(num != 0) and ((num % 10) * \
             (10**int(math.log(num, 10))) + \
                          palindrome(num // 10))
if __name__=="__main__":
    num = int(input("Enter a number to check for Palindrome\t"))
    print ("The original number is : " + str(num))
    res = num == palindrome(num)
    print ("Is the number palindrome ? : " + str(res))