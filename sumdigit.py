def digitSum():
   n = int(input("enter a number:\t"))
   sum=0
   for i in str(n):
       sum +=int(i)
   print("Sum of Digits",n, "is\t",sum)       
        
if __name__=="__main__":
    digitSum()
