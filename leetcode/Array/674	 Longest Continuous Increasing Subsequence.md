# 题目描述

[原题链接](https://leetcode.com/problems/longest-continuous-increasing-subsequence/)

Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).
```
Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.

Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
```

<!--more-->

# 分析
水题，只需要一遍循环即可。主要就是记录状态。

# 代码
空间复杂度O(1),时间复杂度O(n)
```C++
class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        int length = nums.size();
        if(length==0){
            return 0;
        }
        int max_length = 1;
        int current_length = 1;
        for(int i=1;i<length;i++){
            if(nums[i]>nums[i-1]){
                current_length ++;
            }else{
                max_length = max(current_length,max_length);
                current_length = 1;
            }
        }
        max_length = max(current_length,max_length);
        return max_length;
    }
};
```
