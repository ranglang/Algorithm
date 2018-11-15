# 题目描述

[原题链接](https://leetcode.com/problems/pascals-triangle/)

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

```
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```

<!--more-->

# 分析
水题，本质上构建好，金字塔的顶层即可。

# 代码
空间复杂度O(1),时间复杂度O(n)
```C++
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> result;
        if(numRows == 0){
            return result;
        }
        result.push_back(vector<int> {1});
        if(numRows == 1){
            return result;
        }
        result.push_back(vector<int> {1,1});
        if(numRows == 2){
            return result;
        }
        for(int row=3;row<=numRows;row++){
            vector<int> one_row;
            one_row.push_back(1);
            for(int col=1;col<row-1;col++){
                one_row.push_back(result[row-2][col-1]+result[row-2][col]);
            }
            one_row.push_back(1);
            result.push_back(one_row);
        }
        return result;
    }
};
```
