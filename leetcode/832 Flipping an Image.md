# 题目描述

[原题链接](https://leetcode.com/problems/flipping-an-image/description/）
Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

```
Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
```

<!--more-->

# 分析
按照题目的意思做就行。

需要注意的主要有两个地方:
1. 如何将一行数倒序！对于奇偶数的处理，实际上是(length+1)/2
2. 0->1 1->0 可以通过^运算。异或。

# 代码
```C++
class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
        int rows = A.size();
        if(rows==0){
            return A;
        }
        int cols = A[0].size();
        int half_cols = (cols+1)/2;
        for(int i=0;i<rows;i++){
            for(int j=0;j<half_cols;j++){
                int temp = A[i][j]^1;
                A[i][j] = A[i][cols-1-j]^1;
                A[i][cols-1-j] = temp;
            }
        }
        return A;
    }
};
```