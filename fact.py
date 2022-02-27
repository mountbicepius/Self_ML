def factorial():
   n = int(input("enter a val:\t"))
   ft =1
   for i in range(1,n+1):
       ft=ft*i
   print(ft)       
        
if __name__=="__main__":
    factorial()
