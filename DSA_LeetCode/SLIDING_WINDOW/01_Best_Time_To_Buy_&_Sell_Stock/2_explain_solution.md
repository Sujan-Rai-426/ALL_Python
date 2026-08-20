
># STEPS EXPLAIN: 

1. Take the price list (i.e. `price_list`): Receive a list of stock prices where each index represents a day.

2. Set up pointers: Create two pointers (`buy_day` and `sell_day`) and initialize both at day 0.

3. Initialize profit: Create a variable `max_profit` and set it to 0.

4. Loop through the days (`sell_day`):

    - Update buy day: If the current price is lower than your buy price (`price_list[sell_day]` < `price_list[buy_day]`)<br>
        move `buy_day` to `sell_day` to lock in a cheaper price.
    - Calculate `profit`: Find the `profit` for the current day (`price_list[sell_day]` - `price_list[buy_day]`).
    - Update maximum profit (`max_profit`): Keep the highest profit seen so far (`max_profit` = max(`profit`, `max_profit`)).

5. Return result: Once the loop ends, return `max_profit`.




<!-- STEPS: 

1. Take the list of price (i.e. `price_list`) in order of days. [NOTE: index of `price_list` denotes the day]

2. Create two pointer [i.e. `buy_day` and `sell_day`]
    > `buy_day` pointer will point when to buy the stock. And `sell_day` pointer will point when to sell the stock.<br>
    > Initially place both pointer at 0<sup>th</sup> day. [i.e. `buy_day`, `sell_day` = 0, 0 ]

3. Make variable to store the maximum profit. [i.e. `max_profit`] and initially the `max_profit` will be 0.

4. Now run the loop for `sell_day` till it reaches end price of `price_list` and Check all conditions below:
    - If price in `sell_day` is smaller than price in `buy_day` **(i.e. `price_list[sell_day]` < `price_list[buy_day]`)**, <br> than we need to move `buy_day` to `sell_day` **(i.e. `buy_day` = `sell_day`)** inorder to buy stock in least possible price for more profit. 
    - Also in each loop of `sell_day` we also need to check the `profit` to see how much profit if we sell that day. (i.e. `profit` = `price[sell_day]` - `price[buy_day]`).
    - And in each loop after checking `profit`, we need to assign the `max_profit` value among the previous `max_profit` and current `profit`. <br> **(i.e. `max_profit` = max(`profit`, `max_profit`))**
    - At last end of loop return the `max_profit`.
 -->
