
# 题目描述
[原题链接](https://leetcode.com/problems/contains-duplicate-ii/)

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
```
Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
```

<!--more-->

# 分析
水题，只需要用一个map记录即可。当然也可以用一个set，只保留最近的k个数字。

# 代码
空间复杂度O(n),时间复杂度O(n)
```C++
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        map<int ,int> m;
        int len = nums.size();
        for(int i=0;i<len;i++){
            if(m.find(nums[i])!=m.end()){
                if(i - m[nums[i]] <= k ){
                    return true;
                }
            }
            m[nums[i]] = i;
        }
        return false;
    }
};
```
            