def maxProfit(price_list):
    
    # 'buy_day' pointer to point buy day and 'sell_day' pointer to point sell day
    buy_day = 0   
    sell_day = 0
    
    max_profit = int() # variable to store maximum profit
    
    for sell_day in range(len(price_list)):
        if price_list[sell_day] < price_list[buy_day]:
            buy_day=sell_day
        
        profit = price_list[sell_day] - price_list[buy_day]
        max_profit = max(profit, max_profit)
    
    return max_profit
    


# CALLING Above function
raw_price_list = input("[Enter your price list seperated by comma (,) according to days : \n")
organized_price_list = [int(price.strip()) for price in raw_price_list.split(",")]

print(f"\nInput list: {organized_price_list} \nOutput: Max profit = {maxProfit(organized_price_list)}")