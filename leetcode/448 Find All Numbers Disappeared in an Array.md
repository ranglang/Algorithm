# 题目描述

[原题链接](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/)

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

```
Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
```

<!--more-->

# 分析
因为都是非负的整数，所以如果这个数已经出现了，就在这个值对应的索引上做文章，比如变成复数

# 代码
空间复杂度O(1),时间复杂度O(n)
```C++
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int len = nums.size();
        for(int i=0;i<len;i++){
            if(nums[abs(nums[i])-1] > 0){
                nums[abs(nums[i])-1] *= -1 ;
            }
        }
        vector<int> result;
        for(int i=0;i<len;i++){
            if(nums[i]>0){
                result.push_back(i+1);
            }
        }
        return result;
    }
};
```
