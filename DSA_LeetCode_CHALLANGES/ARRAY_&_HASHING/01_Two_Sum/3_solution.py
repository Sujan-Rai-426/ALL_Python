# 001. Two Sum

def twoSum(num_list, target):
    seen_dict = {}
    l=0
    
    for l, num in enumerate(sorted(num_list)):
        need = target - num
        if need in seen_dict:
            return [seen_dict[need], l]
        
        seen_dict[num]=l #It store character(i.e. num) with index(i.e. l) in seen dictionary in every loop.
    return


target_num = int(input('Enter your targeted num : '))
raw_num_List = input("Enter list of your number seperated by comma(,) : ")
organized_num_list = [int(item.strip()) for item in raw_num_List.split(",")]
print(f"Input List: {organized_num_list} , Target: {target_num}")
print(f"Output: {twoSum(organized_num_list, target_num)} ")