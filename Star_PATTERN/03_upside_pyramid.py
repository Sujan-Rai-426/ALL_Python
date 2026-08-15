# NOTE: If row = 3
#  * * *
#   * *
#    *

row=int(input("Enter number of rows : "))
for i in range(0, row):
    print(" "*i, "* "*(row-i))