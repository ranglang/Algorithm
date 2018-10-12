# 题目描述

[原题链接](https://leetcode.com/problems/max-consecutive-ones/description/)

Given a binary array, find the maximum number of consecutive 1s in this array.

```
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
```

<!--more-->

# 分析
直接线性扫描就行，需要注意的是，最后还需要将count_one和max_one比较一次
或者更简单的方法是在数组最后加一个0也行

# 代码
空间复杂度O(1),时间复杂度O(n)
```C++
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        nums.push_back(0);
        int len = nums.size();
        int max_one = 0;
        int count_one = 0;
        for(int i=0;i<len;i++){
            if(nums[i]){
                count_one++;
            }else{
                if(count_one>max_one){
                    max_one = count_one;
                }
                count_one = 0;
            }
        }
        return max_one;
    }
};
```
