#by anirudh

def handlerFunc():
    row = int(input('Enter the number of rows: '))
    col = int(input('Enter the number of columns: '))
    # Initialize matrix
    matrix = []
    print("Enter the entries rowwise:")

    # For user input
    for i in range(row):# A for loop for row entries
        a =[]
        for j in range(col):# A for loop for column entries
             a.append(int(input()))
        matrix.append(a)

    # For printing the matrix
    for i in range(row):
        for j in range(col):
            print(matrix[i][j], end = " ")
        print()
    
if __name__=="__main__":
    handlerFunc()