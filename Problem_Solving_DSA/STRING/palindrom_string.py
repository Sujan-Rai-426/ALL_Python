# NOTE:To identify if the given string is palindrom or not
# EXAMPLE: If input "racecar" => return True
# EXAMPLE: If input "raceca" => return False


def is_Palindrom_Str( strs ):
    return strs == strs[::-1]


message = input("Enter your string: ")
print("\nPalindrom status ", is_Palindrom_Str(message))