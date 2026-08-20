
# 125. Valid Palindrome

def validPalindrome( message ):
    l = 0
    r = len(message) - 1
    is_palindrome = True
    
    while l < r:
        if message[l] != message[r]:
            is_palindrome = False
        
        l += 1
        r -= 1
    
    return is_palindrome


# FUNCTION CALL and use
raw_text_message = input("Enter your message: ")
filtered_text_message = raw_text_message.replace(" ", "") #Without any spaces, so spaces don't affect result
print(f"Your message = {raw_text_message} \nPalindrom = { validPalindrome(filtered_text_message) }")



