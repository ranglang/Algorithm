# 题目描述

[原题链接](https://leetcode.com/problems/majority-element/description/)

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
```
Input: [3,2,3]
Output: 3
```

<!--more-->

# 分析
如果一个数字占绝大多数，它通过依次抵消的话，应该还会还会存留

# 代码
空间复杂度O(1),时间复杂度O(n)
```C++
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int current = nums[0];
        int count = 1;
        int length = nums.size();
        for(int i=1;i<length;i++){
            if(nums[i]==current){
                count++;
            }else{
                count--;
                if(count<0){
                    current = nums[i];
                    count = 1;
                }
            }
        }
        return current;
    }
};
```
