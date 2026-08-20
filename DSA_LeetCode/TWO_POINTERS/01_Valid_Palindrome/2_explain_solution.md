
># > # Explain Solution [ 125. Valid Palindrome ]


### Steps:

1. Take message string as input. (e.g., `raw_message` = "race car")

2. Clean the message by removing spaces so they do not affect the result. (`filtered_message` = "racecar")

3. Initialize two pointers (i.e. `l` and `r`)
    > `l` is the left pointer which is at the starting of the `message`. (`l` = 0) <br>
    > `r` is the right pointer which is at the end of the `message`. (`r` = len(`message`) - 1)

4. Initialize a boolean tracking variable to assume the `message` is a palindrome initially.
    > `is_palindrome` = True

5. Run a while loop as long as the left pointer is less than the right pointer (`l` < `r`).
    > Check if characters match: if `message`[`l`] != `message`[`r`]: <br>
    > If they don't match, update `is_palindrome` = False. <br>
    > Move both pointers inward (`l` += 1 and `r` -= 1).

6. Return the final `is_palindrome` result once the pointers meet.