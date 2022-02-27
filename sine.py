import math


def showSine(val):
    print(math.sin(val))

if __name__=="__main__":
    val = int(input("Enter value of angle in degrees\t"))
    showSine(val)
