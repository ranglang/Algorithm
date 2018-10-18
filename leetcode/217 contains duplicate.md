21# 题目描述

[原题链接](https://leetcode.com/problems/contains-duplicate/)

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
```
Input: [1,2,3,1]
Output: true

Input: [1,2,3,4]
Output: false

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
```

<!--more-->

# 分析
hash set 可以解决。就是判断这个数在之前是否出现，本质是一个搜索问题。所以也可以通过先排序解决。

# 代码
空间复杂度O(n),时间复杂度O(n)
```C++
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> s;
        int length = nums.size();
        for(int i=0;i<length;i++){
            if(s.find(nums[i]) == s.end()){
                s.insert(nums[i]);
            }else{
                return true;
            }
        }
        return false;
    }
};
```
