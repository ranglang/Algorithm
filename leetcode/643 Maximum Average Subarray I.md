# 题目描述

[原题链接](https://leetcode.com/problems/maximum-average-subarray-i/)

Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

```
Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

```

<!--more-->

# 分析
水题，相当于窗口依次移动

# 代码
空间复杂度O(1),时间复杂度O(n)
```C++
class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int len = nums.size();
        int temp_sum = 0;
        for(int i=0;i<k;i++){
            temp_sum += nums[i];
        }
        int max_sum = temp_sum;
        for(int i=k;i<len;i++){
            temp_sum = temp_sum - nums[i-k] + nums[i];
            max_sum = max(max_sum,temp_sum);
        }
        return max_sum*1.0/k;
    }
};
```
