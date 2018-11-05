# 题目描述

[原题链接](https://leetcode.com/problems/magic-squares-in-grid/)

A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

```
Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15
```

<!--more-->

# 分析
如果一个矩阵是magic矩阵，那么它正中的数字一定是5.

因为1～9的和是45，所以每一行的数字和是15.

经过中心的线一共有4条，和是60，而这些刚好是 45 + 3*中间数字 = 60 所以中间的数字是5

所以如果一个数字是5，下面就是核实的问题了，先确定数字的唯一性，再确定各个方向的加和是不是等于15

# 代码
空间复杂度O(1),时间复杂度O(n)
```C++
class Solution {
public:
    int numMagicSquaresInside(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid.size();
        int magic_matrix_count = 0;
        for(int i=1;i<rows-1;i++){
            for(int j=1;j<cols-1;j++){
                if(grid[i][j]==5){
                    vector<int> book(10,0);
                    book[5] = 1;
                    // 先检查元素是否合格
                    int next[8][2] = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
                    bool is_num_valid = true;
                    for(int k=0;k<8;k++){
                        if(!check_num_is_valid(book,grid,i+next[k][0],j+next[k][1])){
                            is_num_valid = false;
                            break;
                        }
                    }
                    if(!is_num_valid){
                        continue;
                    }
                    // 检查加和是否正确
                    if(grid[i-1][j-1] +grid[i-1][j] + grid[i-1][j+1] == 15 &&
                       grid[i][j-1] +grid[i][j] + grid[i][j+1] == 15 &&
                       grid[i+1][j-1] +grid[i+1][j] + grid[i+1][j+1] == 15 &&
                       grid[i-1][j-1] + grid[i][j-1] + grid[i+1][j-1] == 15 &&
                       grid[i-1][j] + grid[i][j] + grid[i+1][j] == 15 &&
                       grid[i-1][j+1] + grid[i][j+1] + grid[i+1][j+1] == 15 &&
                       grid[i-1][j-1] + grid[i+1][j+1] == 10 &&
                       grid[i-1][j+1] + grid[i+1][j-1] == 10
                      ){
                        magic_matrix_count ++;
                    }
                }
            }
        }
        return magic_matrix_count;
    }
    
    bool check_num_is_valid(vector<int>& book,vector<vector<int>>& grid,int i,int j){
        if(grid[i][j] <= 9 && grid[i][j] >0 && book[grid[i][j]] == 0){
            book[grid[i][j]] = 1;
            return true;
        }else{
            return false;
        }
    }
    
};
```
