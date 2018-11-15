# 题目描述

[原题链接](https://leetcode.com/problems/positions-of-large-groups/description/)

In a string S of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

The final answer should be in lexicographic order.

```
IInput: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.

Input: "abc"
Output: []
Explanation: We have "a","b" and "c" but no large group.
```

<!--more-->

# 分析
水题，只需要遍历一遍，判断后一个是不是跟前一个相同即可

# 代码
空间复杂度O(1),时间复杂度O(n)
```C++
class Solution {
public:
    vector<vector<int>> largeGroupPositions(string S) {
        int length = S.size();
        int begin = 0 ;
        int end = 0;
        vector<vector<int>> result;
        for(int i=1;i<length;i++){
            if(S[i]==S[i-1]){
                end = i;
            }else{
                if((end-begin+1)>=3){
                    result.push_back(vector<int>({begin,end}));
                }
                begin = i;
                end = i;
            }
        }
        if((end-begin+1)>=3){
            result.push_back(vector<int>({begin,end}));
        }
        return result;
    }
};
```
