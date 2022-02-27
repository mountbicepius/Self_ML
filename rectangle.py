def showrect():
    print("Welcome, we are going to print a numeric rectangle for\na given width and height")
    x = int(input("Enter width of rectangle: "))
    y = int(input("Enter height of rectangle: "))
    k = 0
    for _ in range(y):
        for _ in range(x):
            print(k, end=' ')
            k += 1
            if k == 10:
                k = 0
        print("")

if __name__=="__main__":
    showrect()