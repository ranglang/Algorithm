# 题目描述

[原题链接](https://leetcode.com/problems/degree-of-an-array/)

Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

```
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
```

<!--more-->

# 分析
建立三个map，分别记录开始，结束和出现数目

# 代码
空间复杂度O(n),时间复杂度O(n)
```C++
class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        map<int,int> start_m;
        map<int,int> end_m;
        map<int,int> count_m;
        int len = nums.size();
        for(int i=0;i<len;i++){
            if(start_m.find(nums[i])==start_m.end()){
                start_m[nums[i]] = i;
                count_m[nums[i]] = 0;
            }
            count_m[nums[i]] ++;
            end_m[nums[i]] = i;
        }
        int max_count = 0;
        int max_count_num=0;
        int min_distance = len;
        for(auto it=count_m.begin();it!=count_m.end();it++){
            if((it->second > max_count) || (it->second ==  max_count && end_m[it->first] - start_m[it->first] < min_distance) ){
                max_count = it->second;
                max_count_num = it->first;
                min_distance = end_m[it->first] - start_m[it->first];
            }
        }
        return min_distance+1;
    }
};
```
