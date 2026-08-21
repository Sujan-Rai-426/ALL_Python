
# NOTE: 11. Container With Most Water
def maxArea(wall_height):
    l, r = 0, len(wall_height)-1
    max_Area = int()
    
    while l < r:
        area = ( (min(wall_height[l], wall_height[r])) * (r-l) )
        max_Area = max(max_Area, area)
        if wall_height[l] < wall_height[r]:
            l += 1
        else:
            r -= 1
    
    return max_Area


# Function call.
raw_wall_height_list = input("Enter list of height of wall seperated by comma (,) : ")
organized_wall_height_list =  [int(height.strip()) for height in raw_wall_height_list.split(",")]

print(f"Wall height list = {organized_wall_height_list} \nOutput: {maxArea(organized_wall_height_list)}")