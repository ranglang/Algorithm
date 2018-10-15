# 题目描述

[原题链接](https://leetcode.com/problems/move-zeroes/discuss/)

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

```
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
```

<!--more-->

# 分析
新增一个index就专门记录非0的元素即可

# 代码
空间复杂度O(n),时间复杂度O(1)
```C++
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int non_zero_index = 0;
        int len = nums.size();
        for(int i=0;i<len;i++){
            if(nums[i]!=0){
                nums[non_zero_index++] = nums[i];
            }
        }
        for(;non_zero_index<len;non_zero_index++){
            nums[non_zero_index] = 0;
        }
    }
};
```
