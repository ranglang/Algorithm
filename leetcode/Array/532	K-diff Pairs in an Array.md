
# 题目描述
[原题链接](https://leetcode.com/problems/k-diff-pairs-in-an-array)

Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

```
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
```

<!--more-->

# 分析
通过map可以解决，需要注意的是几种用法，比如遍历数组，还有遍历map，还有count这种操作

# 代码
空间复杂度O(n),时间复杂度O(n)
```C++
class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        if(k<0){
            return 0;
        }
        unordered_map<int,int> m;
        for (int n : nums) m[n]++;
        int cnt = 0;
        for (auto p : m) {
          if ((!k && p.second > 1)
            || (k && m.count(p.first + k))) ++cnt;
        }
        return cnt;
        
    }
};
```
            