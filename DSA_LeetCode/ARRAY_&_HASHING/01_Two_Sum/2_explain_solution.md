
># > # Explain Solution [ 1. Two Sum ] 

**Steps we need to be followed :**

### Input from user:
1. list of `num` :- **eg. `num_list`**
2. target sum :- **eg. `target`**

### Function [Solution Approach]
- **`seen_dict = {}:`** A dictionary that acts as memory to store numbers we've already checked (with the number (i.e. `num`) as the key and its index (i.e. `l`) as the value).

- **enumerate(sorted(num_list)):** Sorts the list first, then loops through every number (`num`) and its index (`l`).

- **`need` = `target` - `num`:** Calculates what number is missing to reach the target sum.

- if need in `seen_dict::` Checks if we have already saved that missing number. If yes, we found our pair and it returns their indices: [`seen_dict[need], l`].

- **`seen_dict[num] = l:`** If the missing number isn't found yet, it saves the current number and its index into the dictionary for the next loops.



<!-- ### Function [Solution Approach]
- Create empty dictionary {} **[eg. seen_dict = {}]** 
- Run the loop using `enumerate` in **num_list** to get both `index` and `num` of list.
- needed_num = target - num
- In each loop check if `needed num` exist in `seen_dict`. If not than store that `num` in `seen_dict` along with its `index`.  ***seen_dict[num]=index***
- If `needed num` exist in `seen_dict` than return the `index` value of `needed_num` from `seen_dict` And current `index` in `num_list` -->