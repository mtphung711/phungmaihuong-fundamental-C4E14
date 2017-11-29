row = int(input("enter number of rows"))
column = int(input("enter number of columns"))

for i in range(row):
    for j in range(column):
        if (i + j) % 2 == 0:
            print("*", end = ' ')
        else:
            print("x", end = ' ')

    print("\r")
