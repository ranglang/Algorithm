# 题目描述

[原题链接](https://leetcode.com/problems/maximum-subarray/)

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

```
Example:

Input: 3
Output: [1,3,3,1]
```

<!--more-->

# 分析
输出的是制定的行。
有一个公式 对于第 C(n,k) = n!/k!(n-k)!

# 代码
空间复杂度O(n),时间复杂度O(n)
```C++
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> result(rowIndex+1,0);
        result[0] = 1;
        result[rowIndex] = 1;
        int half_len = rowIndex/2 + 1;
        for(int i=1;i<half_len;i++){
            result[i] = result[rowIndex-i] = result[i-1]  * (unsigned long)(rowIndex-i+1) / (unsigned long)i ;
        }
        return result;
    }
};        
```
