# 题目描述

[原题链接](https://leetcode.com/problems/two-sum/)

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

```
Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

```

<!--more-->

# 分析
因为是无序的，所以与之前的做法是不一样的。
这里需要一个hash map，value_to_index
然后一遍遍历，一边向前查找是否有合适的值相加等于target

# 代码
空间复杂度O(n),时间复杂度O(n)
```C++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int len = nums.size();
        map<int,int> value_to_index ;
        vector<int> result;
        for(int i=0;i<len;i++){
            int left = target-nums[i];
            if(value_to_index.find(left) != value_to_index.end() && value_to_index[left] != i ){
                result.push_back(value_to_index[left]);
                result.push_back(i);
                return result;
            }
            value_to_index[nums[i]] = i;
        }
        return result;
    }
};
```
