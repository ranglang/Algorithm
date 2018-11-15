
# 题目描述
[原题链接](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/)

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

```
Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
```

<!--more-->

# 分析
一开始的想法就是排序，然后对比一下原来的数组，就能找到最小需要调整的序列了

实际上的做法是，找到乱序部分的最大数和最小数，然后看需要插入在什么位置，这样是O(n)

# 代码
基于排序的算法

空间复杂度O(n),时间复杂度O(nlogn)
```C++
class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        vector<int> sorted_num(nums.begin(),nums.end());
        sort(sorted_num.begin(),sorted_num.end());
        int len = nums.size();
        int start = -1;
        int end = 0;
        for(int i=0;i<len;i++){
            if(nums[i]!=sorted_num[i]){
                start = i;
                break;
            }
        }
        if(start==-1)
            return 0;
        for(int i=len-1;i>=0;i--){
            if(nums[i]!=sorted_num[i]){
                end = i;
                break;
            }
        }
        return end-start+1;
    }
};
```

O(n)的算法
```C++
class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        int len = nums.size();
        bool flag = false;
        int min_num = INT_MAX;
        int max_num = INT_MIN;
        for(int i=1;i<len;i++){
            if(nums[i] < nums[i-1]){
                flag = true;
            }
            if(flag){
                min_num = min(min_num,nums[i]);
            }
        }
        flag = false;
        for(int i=len-2;i>=0;i--){
            if(nums[i] > nums[i+1]){
                flag = true;
            }
            if(flag){
                max_num = max(max_num,nums[i]);
            }
        }
        int l = -1;
        int r = -1;
        for(int i=0;i<len;i++){
            if(nums[i]>min_num){
                l = i;
                break;
            }
        }
        if(l==-1){
            return 0;
        }
        for(int i=len-1;i>=0;i--){
            if(nums[i]<max_num){
                r = i;
                break;
            }
        }
        return r-l+1;
    }
};
```