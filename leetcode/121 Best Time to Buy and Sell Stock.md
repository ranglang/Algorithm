# 题目描述

[原题链接](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/)

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
```
Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

<!--more-->

# 分析
核心是找到  max(price[j] - price[i]) j>i

通过一遍遍历即可，记录下最大利润和当前最小的价格

# 代码
空间复杂度O(1),时间复杂度O(n)
```C++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int length = prices.size();
        int min_price = INT_MAX;
        int max_profit = 0;
        for(int i=0;i<length;i++){
            if(prices[i]<min_price){
                min_price = prices[i];
            }else{
                max_profit = max(max_profit,prices[i]-min_price);
            }
        }
        return max_profit;
    }
};
```
