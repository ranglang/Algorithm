
# 题目描述
[原题链接](https://leetcode.com/problems/rotate-array)

Given an array, rotate the array to the right by k steps, where k is non-negative.

```
Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

<!--more-->

# 分析
实际上需要做的事情非常简单，3次翻转即可。

# 代码
空间复杂度O(1),时间复杂度O(n)
```C++
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int len = nums.size();
        k = k % len;
        if(k==0) return;
        reverse(nums,0,len-k-1);
        reverse(nums,len-k,len-1);
        reverse(nums,0,len-1);
    }
    
    void reverse(vector<int>& nums,int start,int end){
        while(start<end){
            swap(nums[start],nums[end]);
            start++;
            end--;
        }
    }
    
};
```
            