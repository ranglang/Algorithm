# 题目描述

[原题链接](https://leetcode.com/problems/image-smoother/description/)

Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.
```
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
```

<!--more-->

# 分析
水题，遍历整个矩阵即可

# 代码
空间复杂度O(n),时间复杂度O(n)
```C++
class Solution {
public:
    vector<vector<int>> imageSmoother(vector<vector<int>>& M) {
        int rows = M.size();
        int cols = M[0].size();
        vector<vector<int>> result(rows,vector<int>(cols,0));
        int surround[9][2] = {{-1,-1},{0,-1},{1,-1},{-1,0},{0,0},{1,0},{-1,1},{0,1},{1,1}};
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                int sum = 0;
                int valid_count = 0;
                for(int k=0;k<9;k++){
                    int new_x = i + surround[k][0];
                    int new_y = j + surround[k][1];
                    if(new_x >= 0  && new_x < rows && new_y >=0 && new_y < cols){
                        sum += M[new_x][new_y];
                        valid_count ++;
                    }
                }
                result[i][j] = sum / valid_count;
            }
        }
        return result;
    }
};
```
