# 题目描述

[原题链接](https://leetcode.com/problems/transpose-matrix/description/)

Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.



```
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
```

<!--more-->

# 分析
直接复制就行，原来矩阵中的第i行第j列，是转置后矩阵的第j行第i列

需要注意的是，可以直接先开辟一个vector空间

# 代码
空间复杂度O(n2),时间复杂度O(n2)
```C++
class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& A) {
        int rows = A.size();
        int cols = A[0].size();
        vector<vector<int>> new_matrix(cols,vector<int>(rows,0));
        for(int i=0;i<rows;i++){
           for(int j=0;j<cols;j++){
               new_matrix[j][i] = A[i][j];
           }
        }
        return new_matrix;
    }
};
```
