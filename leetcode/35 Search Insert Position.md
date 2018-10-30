# 题目描述

[原题链接](https://leetcode.com/problems/search-insert-position/)

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

```
Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
```

<!--more-->

# 分析
水题，简单的二分查找

# 代码
空间复杂度O(1),时间复杂度O(n)
```C++
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int length = nums.size();
        int right = length -1 ;
        int left = 0;
        while(left<=right){
            int mid = (left+right) / 2;
            if(nums[mid]<target){
                left = left+1;
            }else if(nums[mid]>target){
                right = right-1;
            }else{
                return mid;
            }
        }
        return left;
    }
};
```
