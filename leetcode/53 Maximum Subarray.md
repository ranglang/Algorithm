# 题目描述

[原题链接](https://leetcode.com/problems/maximum-subarray/)

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

```
Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

<!--more-->

# 分析
水题，仅仅需要计算当前最大的值即可。本质是一个dp的问题。

# 代码
空间复杂度O(1),时间复杂度O(n)
```C++
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int len = nums.size();
        int current_sum = nums[0];
        int max_sum = nums[0];
        for(int i=1;i<len;i++){
            if(current_sum<0){
                current_sum = nums[i];
            }else{
                current_sum += nums[i];
            }
            max_sum = max(max_sum,current_sum);
        }
        return max_sum;
    }
};
```
