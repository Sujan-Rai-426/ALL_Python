

># Explain Solution [ 344. Reverse String ]

## Steps:

1. Take a list of characters as input. (e.g., `str_list` = `["h", "e", "l", "l", "o"]`)

2. Initialize two pointers (`l` and `r`) to track the positions from both ends.
    > `l` is the left pointer starting at the beginning of the list. (`l` = 0) <br>
    > `r` is the right pointer starting at the end of the list. (`r` = len(`str_list`) - 1)

3. Run a while loop as long as the left pointer is strictly less than the right pointer (`l` < `r`).
    > ### Swap the elements at the two pointers in-place:
    > `str_list`[`l`], `str_list`[`r`] = `str_list`[`r`], `str_list`[`l`]

4. Move both pointers toward the center.
    > Increment the left pointer (`l` += 1) <br>
    > Decrement the right pointer (`r` -= 1)

5. Return the reversed `str_list` once the pointers meet or cross each other in the middle.
