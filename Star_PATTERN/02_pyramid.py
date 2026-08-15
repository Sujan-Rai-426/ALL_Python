# NOTE: if row = 3
#   *
#  * *
# * * * 


row = int(input("Enter number of rows : "))

for i in range( 1, row+1 ):
    print ( " " * (row-i), "* " * i )