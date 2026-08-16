
# TODO: To check if the given string is palindrom or not.
# NOTE: i pointer at star and j pointer at end. When letter of each index are equal than increase i pointer by 1 and decrease j pointer by 1. and when both i and j pointer meet or cross eachother than stop loop. If no equal state palindrom as false else true.

word=input("Enter your word without space " " to check its pallindrom property : ")  

i=0     # i index at starting of word
j=len(word)-1   # j index at ending of word
is_Palindrom = True  

while i<j:
    if word[i] != word[j]:
        is_Palindrom = False
    i+=1
    j-=1

print(is_Palindrom)