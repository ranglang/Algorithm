# 题目描述

[原题链接](https://leetcode.com/problems/reshape-the-matrix/description/)

In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.



```
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.

Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
```

<!--more-->

# 分析
直接简单的重新进行堆叠就行。

# 代码
空间复杂度O(N*M),时间复杂度O(N*M)
```C++
class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& nums, int r, int c) {
        int rows = nums.size();
        int cols = nums[0].size();
        if(rows*cols != r*c){
            return nums;
        }
        vector<vector<int>> new_matrix(r,vector<int>(c,0));
        int new_i = 0;
        int new_j = 0;
        for(int i =0;i<rows;i++){
            for(int j=0;j<cols;j++){
                new_matrix[new_i][new_j] = nums[i][j];
                if(new_j == c-1){
                    new_i += 1;
                    new_j = 0;
                }else{
                    new_j += 1;
                }
            }
        }
        return new_matrix;
    }
};
```

