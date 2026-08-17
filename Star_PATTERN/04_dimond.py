# NOTE: If row = 3
#    *
#   * *
#  * * *
#   * *
#    *


row = int(input("Enter number of rows : "))
for i in range(row+1):
    print( " " * (row - i), "* " * i)
    
for j in range(1, row):
    print(" " * j, "* " * (row-j))