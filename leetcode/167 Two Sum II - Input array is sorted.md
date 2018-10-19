# 题目描述

[原题链接](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.

```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
```

<!--more-->

# 分析
直接线性扫描就行,因为一定有答案。
所以我们可以认为一个从前一个从后面，如果比目标值小，那一定要前面的向后移动，如果比目标值大，后面的一定要先前移动，知道获得了目标值。

# 代码
空间复杂度O(1),时间复杂度O(n)
```C++
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int length = numbers.size();
        int left = 0;
        int right = length-1;
        while(numbers[left] + numbers[right] != target){
            if(numbers[left] + numbers[right] < target){
                left++;
            }else{
                right--;
            }
        }
        return vector<int>({left+1,right+1});
    }
};
```
