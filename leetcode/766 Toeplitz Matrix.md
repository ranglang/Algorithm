# 题目描述

[原题链接](https://leetcode.com/problems/toeplitz-matrix/description/)

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

```
Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
```

<!--more-->

# 分析
一开始比较蠢，想着就沿着对角线验证，后来又思考了一下可以通过递归来验证，但是需要构建一个子矩阵，这边是简单复制操作的，所以浪费了空间，C++水平还不够啊

实际上这道题，只需要逐个验证即可，依旧是当前元素和左上的元素是否相等就行，当然左上的元素需要存在。

# 代码
空间复杂度O(M*N),时间复杂度O(M*N)
```C++
class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        int rows = matrix.size();
        if(rows<=1){
            return true;
        }
        int cols = matrix[0].size();
        if(cols<=1){
            return true;
        }
        vector<vector<int>> sub_matrix(rows-1,vector<int>(cols-1,0));
        for(int i=0;i<rows-1;i++){
            for(int j=0;j<cols-1;j++){
                sub_matrix[i][j] = matrix[i][j];
            }
        }
        for(int i=1;i<rows;i++){
            if(matrix[i][cols-1] != matrix[i-1][cols-2]){
                return false;
            }
        }
        for(int j=1;j<cols-1;j++){
            if(matrix[rows-1][j] != matrix[rows-2][j-1]){
                return false;
            }
        }
        return isToeplitzMatrix(sub_matrix);
    }
};
```
空间复杂度O(1),时间复杂度O(M*N)
```C++
class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        int rows = matrix.size();
        int cols = matrix[0].size();
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if(i>0 && j>0 && matrix[i][j] != matrix[i-1][j-1]){
                    return false;
                }
            }
        }
        return true;
    }
};
```
