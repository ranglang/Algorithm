# 题目描述

[原题链接](https://leetcode.com/problems/largest-number-at-least-twice-of-others/)

In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

```
Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
 

Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.

```

<!--more-->

# 分析
水题，只需要记录下最大的前两个数即可。
# 代码
空间复杂度O(1),时间复杂度O(n)
```C++
class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        int length = nums.size();
        int max_1 = nums[0];
        int max_2 = INT_MIN;
        int max_1_index = 0;
        for(int i=1;i<length;i++){
            if(nums[i]>max_2){
                max_2 = nums[i];
                if(max_2 > max_1){
                    max_2 = max_1;
                    max_1 = nums[i];
                    max_1_index = i;
                }
            }
        }
        if(max_1 >= max_2 *2){
            return max_1_index;
        }else{
            return -1;
        }
    }
};
```
