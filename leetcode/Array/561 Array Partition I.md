# 题目描述

[原题链接](https://leetcode.com/problems/array-partition-i/description/)

Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

```
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
```

<!--more-->

# 分析
基础想法就是首先排序，然后间隔的取数即可。

但是排序操作的O(nlogn)的，所以也可以通过以空间换时间的方式，进行"排序"

# 代码
空间复杂度O(1),时间复杂度O(nlogn)
```C++
class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int len = nums.size();
        int result = 0;
        for(int i=0;i<len;i+=2){
            result+=nums[i];
        }
        return result;
    }
};
```
空间复杂度O(n),时间复杂度O(n)
```C++
class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
        int count_len = 10000*2+1;
        vector<int> count (count_len,0);
        int len = nums.size();
        for(int i=0;i<len;i++){
            count[nums[i]+10000] += 1;
        }
        int result = 0;
        int is_first=1;
        for(int i=0;i<count_len;){
            if(count[i]==0){
                i++;
                continue;
            }
            if(is_first){
                result += i-10000;
            }
            count[i]--;
            is_first=is_first^1;
        }
        return result;
    }
};
```
