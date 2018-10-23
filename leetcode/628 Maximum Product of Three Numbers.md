# 题目描述

[原题链接](https://leetcode.com/problems/maximum-product-of-three-numbers/)

Given an integer array, find three numbers whose product is maximum and output the maximum product.

```
Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
```

<!--more-->

# 分析
因为可能存在负数的情况，所以需要找到最小的两个数，和最大的三个数


# 代码
空间复杂度O(1),时间复杂度O(nlogn)
```C++
class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int length = nums.size();
        int max_1 = nums[0]*nums[1]*nums[length-1];
        int max_2 = nums[length-1]*nums[length-2]*nums[length-3];
        return max(max_1,max_2);
    }
};
```

还可以直接只进行一轮遍历，记录下最小的两个数，和最大的三个数

```C++
class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        int min_1 = 1000;
        int min_2 = 1000;
        int max_1 = -1000;
        int max_2 = -1000;
        int max_3 = -1000;
        int len = nums.size();
        for(int i=0;i<len;i++){
            if(nums[i]<=min_2){
                min_2 = nums[i];
                if(min_2<=min_1){
                    exchange(&min_1,&min_2);
                }
            }
            if(nums[i]>=max_3){
                max_3 = nums[i];
                if(max_3>=max_2){
                    exchange(&max_2,&max_3);
                }
                if(max_2>=max_1){
                    exchange(&max_2,&max_1);
                }
            }
        }
        return max(min_2*min_1*max_1,max_2*max_3*max_1);
    }
    
    void exchange(int *p , int *q){
        int ch;
        ch = *p;
        *p = *q;
        *q = ch;
    }
    
};
```
