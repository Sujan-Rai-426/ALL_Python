

># Explain Solution [ 11. Container With Most Water ]

## Steps:

1. Take list of wall height as input. (e.g. `height_list` = [1, 8, 6, 2, 5, 4, 8, 3, 7])

2. Initialize two pointers (i.e. `l` and `r`)
    > `l` is left pointer which is at the starting of the height list. (`l` = 0) <br>
    > `r` is right pointer which is at the end of the height list. (`r` = len(`height_list`) - 1)

3. Initialize memory variable to track maximum area.
    > `max_Area` = 0

4. Run a while loop as long as the left pointer is less than the right pointer (`l` < `r`).
    >### Calculate current area using the formula:
    > `area` = ( min(`height_list`[`l`], `height_list`[`r`]) * (`r` - `l`) ) <br>
    > Update `max_Area` = max(`max_Area`, `area`)

5. Shift the pointer of the shorter wall inward to search for a potentially taller wall.
    > If `height_list`[`l`] < `height_list`[`r`], move left pointer rightward (`l` += 1) <br>
    > Else, move right pointer leftward (`r` -= 1)

6. Return the final `max_Area` once the pointers meet.
