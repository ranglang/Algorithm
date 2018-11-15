# 题目描述

[原题链接](https://leetcode.com/problems/third-maximum-number)

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).
```
Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
```

<!--more-->

# 分析
主要是能不能使用long这个类型,还有学习到一点就是交换函数已经内建了 也就是 swap

# 代码
空间复杂度O(1),时间复杂度O(n)
```C++
class Solution {
public:
    int thirdMax(vector<int>& nums) {
        int len = nums.size();
        int max_1 = nums[0];
        int max_2,max_3;
        bool is_max_2 = true;
        bool is_max_3 = true;
        int index = 1;
        for(;index<len;index++){
            if(is_max_2 && nums[index] != max_1){
                if(nums[index] > max_1){
                    max_2 = max_1;
                    max_1 = nums[index];
                }else{
                    max_2 = nums[index];
                }
                is_max_2 = false;
                continue;
            }
            if(is_max_3 && nums[index] != max_2 && nums[index] != max_1){
                if(nums[index] > max_2){
                    max_3 = max_2;
                    max_2 = nums[index];
                }else{
                    max_3 = nums[index];
                }
                if(max_2 > max_1){
                    swap(max_2,max_1);
                }
                is_max_3 = false;
                break;
            }
        }
        if(is_max_3){
            return max_1;
        }
        index++;
        for(;index<len;index++){
            if(nums[index] == max_1 || nums[index] == max_2 || nums[index] == max_3)
                continue;
            if(nums[index]>max_3){
                max_3 = nums[index];
                if(max_3 > max_2){
                    swap(max_3,max_2);
                    if(max_2 > max_1){
                        swap(max_2,max_1);
                    }
                }
            }
        }
        return max_3;
    }

};
```
