
  
def isPalindrome(s):
    return s == s[::-1]
  
if __name__=="__main__":
    num = str(input("Enter a string to check for Palindrome\t"))
    if isPalindrome(num):
      print('Yes')
    else:
      print('No')