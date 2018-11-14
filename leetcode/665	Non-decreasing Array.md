
# 题目描述
[原题链接](https://leetcode.com/problems/non-decreasing-array/)

Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

```
Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
```

<!--more-->

# 分析
首先查找数组中下降的位置，如果有2个以及以上的位置，则一定是false，如果没有下降的位置，则一定是true

对于一个位置，

如果是0，或者len-1 一定是true

满足nums[i+1] >= nums[i-1] or nums[i+2] >= nums[i] 也是true

剩下的情况就是false


# 代码
空间复杂度O(1),时间复杂度O(n)
```C++
class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int len = nums.size();
        int has_one = false;
        for(int i=0;i<len-1;i++){
            if(nums[i] > nums[i+1]){
                if((i-1 >= 0 && nums[i-1] > nums[i+1]) && (i+2<len && nums[i+2] < nums[i]) ){
                    return false;
                }
                if(has_one){
                    return false;
                }
                has_one = true;
            }
        }
        return true;
    }
};
```
            