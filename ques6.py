import math

def factorialrec(val):
    if val ==0:
        return 1
    elif val==1:
        return val
    return val*factorialrec(val-1)

def factorialmath(val):
    print(math.factorial(val))
        
        
if __name__=="__main__":
    inputval=int(input("Choose relevant option:\n1.show via recursion\n2.show via math function\t"))
    if inputval == 1:
        val=int(input("Enter value for calculating factorial\t"))
        print(factorialrec(val))
    elif inputval == 2:
        val=int(input("Enter value for calculating factorial\t"))
        print(factorialmath(val))
    else:
        print("Invalid option, Try again")