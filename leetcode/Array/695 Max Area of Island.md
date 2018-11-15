# 题目描述

[原题链接](https://leetcode.com/problems/max-area-of-island/description/)

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

```
input
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
 result:6
```

<!--more-->

# 分析
深度优先遍历,不需要采用一个记录是否访问过的数组，因为如果一个岛屿访问过了，直接将这个岛置为0

# 代码
空间复杂度O(M*N),时间复杂度O(1)
```C++
class Solution {
    public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int max_area = 0;
        for(int i = 0; i < grid.size(); i++)
            for(int j = 0; j < grid[0].size(); j++)
                if(grid[i][j] == 1){
                    max_area = max(max_area, AreaOfIsland(grid, i, j));
                }
        return max_area;
    }
    
    int AreaOfIsland(vector<vector<int>>& grid, int i, int j){
        if( i >= 0 && i < grid.size() && j >= 0 && j < grid[0].size() &&  grid[i][j] == 1){
            grid[i][j] = 0;
            return 1 + AreaOfIsland(grid, i+1, j) + AreaOfIsland(grid, i-1, j) + AreaOfIsland(grid, i, j-1) + AreaOfIsland(grid, i, j+1);
        }
        return 0;
    }

    
};
```

下面是BFS的做法
```C++
class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        int max_area = 0;
        int next_step[4][2]={{0,1},{0,-1},{1,0},{-1,0}};
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if(grid[i][j]==1){
                    int current_area = 1;
                    queue<pair<int,int>> q;
                    push_into_queue(grid,q,i,j);
                    while(!q.empty()){
                        int x = q.front().first;
                        int y = q.front().second;
                        q.pop();
                        for(int k=0;k<4;k++){
                            int next_x = x+next_step[k][0];
                            int next_y = y+next_step[k][1];
                            if(next_x >= 0 && next_x < rows && next_y >= 0 && next_y<cols && grid[next_x][next_y]==1){
                                push_into_queue(grid,q,next_x,next_y);
                                current_area++;
                            }
                        }
                    }
                    max_area = max(max_area,current_area);
                }
            }
        }
        return max_area;
    }
    
    void push_into_queue(vector<vector<int>>& grid,queue<pair<int,int>>& q,int x,int y){
        q.push({x,y});
        grid[x][y] = 0;
    }
    
};
```

下面是DFS的做法 非递归的做法
```C++
class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        int max_area = 0;
        int next_step[4][2]={{0,1},{0,-1},{1,0},{-1,0}};
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if(grid[i][j]==1){
                    int current_area = 1;
                    stack<pair<int,int>> s;
                    push_into_stack(grid,s,i,j);
                    while(!s.empty()){
                        int x = s.top().first;
                        int y = s.top().second;
                        s.pop();
                        for(int k=0;k<4;k++){
                            int next_x = x+next_step[k][0];
                            int next_y = y+next_step[k][1];
                            if(next_x >= 0 && next_x < rows && next_y >= 0 && next_y<cols && grid[next_x][next_y]==1){
                                push_into_stack(grid,s,next_x,next_y);
                                current_area++;
                            }
                        }
                    }
                    max_area = max(max_area,current_area);
                }
            }
        }
        return max_area;
    }
    
    void push_into_stack(vector<vector<int>>& grid,stack<pair<int,int>>& s,int x,int y){
        s.push({x,y});
        grid[x][y] = 0;
    }
    
};
```
