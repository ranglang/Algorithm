# 题目描述

[原题链接](https://leetcode.com/problems/remove-element/)

Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

```
Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
```

<!--more-->

# 分析
水题，添加一个“有效索引”的游标即可。

# 代码
空间复杂度O(1),时间复杂度O(n)
```C++
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int len = nums.size();
        int valid_index = 0;
        for(int i=0;i<len;i++){
            if(nums[i]!=val){
                nums[valid_index++] = nums[i];
            }
        }
        return valid_index;
    }
};
```
