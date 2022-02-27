def showpyramid():
    print("Welcome, we are going to print a numeric pyramid for\na given range")
    x = int(input("Enter range of value: "))
    #y = int(input("Enter height of rectangle: "))
    k=0
    for i in range(0,x):
        for j in range(0,i):
            print(' ',end='')
        k+=1
        print(k)

if __name__=="__main__":
    showpyramid()