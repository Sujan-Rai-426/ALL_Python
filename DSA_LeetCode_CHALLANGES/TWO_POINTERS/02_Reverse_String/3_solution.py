# Leetcode Problem No:- 344. Reverse String

# Reverse the given string

# Space Complexity: O(1)
# Time Complexity: O(n)

def reverseString( str_list ):
    l, r = 0, len(str_list)-1
    hold = str()
    while l <= r:
        hold = str_list[l]
        str_list[l] = str_list[r]
        str_list[r] = hold
        l += 1
        r -= 1
    return str_list


# calling function
raw_str_list = input("Enter your string list seperated by comma (,) : ")
organized_str_list = [item.strip() for item in raw_str_list.split(",")]
print(f"Input: {organized_str_list} \nOutput: {reverseString(organized_str_list)} ")