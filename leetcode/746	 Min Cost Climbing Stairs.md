# 题目描述

[原题链接](https://leetcode.com/problems/min-cost-climbing-stairs/)

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.
```
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
```

<!--more-->

# 分析
这是一道动态规划题，典型的爬楼梯。最后一个状态仅仅和前面两个状态有关系。

一开始采用递归做，是超时的。后来改成dp的算法，开了一个等长的数组存储到达每个位置最优的情况。

然而实际上连数组也不需要，因为仅仅和前面两个状态有关系，所以只需要两个变量就行。

# 代码
空间复杂度O(1),时间复杂度O(n)
```C++
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int length = cost.size();
        int f1 = 0, f2=0;
        for(int i=2;i<=length;i++){
            int f0 = min(f2+cost[i-2],f1+cost[i-1]);
            f2 = f1;
            f1 = f0;
        }
        return f1;
    }
};
```

还有一种更优的做法，计算到达这个点，并从这个点开始下一个点的损耗

空间复杂度O(1),时间复杂度O(n)
```C++
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int length = cost.size();
        int f1 = cost[1], f2=cost[0];
        for(int i=2;i<length;i++){
            int f0 = min(f2,f1)+cost[i];
            f2 = f1;
            f1 = f0;
        }
        return min(f1,f2);
    }
};
```
相比于前面的做法，时间更快，少了一次加法运算

