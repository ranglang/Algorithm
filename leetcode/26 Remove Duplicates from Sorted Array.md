# 题目描述

[原题链接](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

```
Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
```

<!--more-->

# 分析
一开始没有注意到这是有序的，所以用hash set的做法，其实如果有序的话，只需要记录当前最新的有效数字即可。


# 代码
空间复杂度O(1),时间复杂度O(n)
```C++
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int len = nums.size();
        if(len==0){
            return 0;
        }
        int valid_index = 0;
        for(int i=1;i<len;i++){
            if(nums[i]!=nums[valid_index]){
                nums[++valid_index] = nums[i];
            }
        }
        return valid_index+1;
    }
};
```
