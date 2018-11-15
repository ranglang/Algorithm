
# 题目描述
[原题链接](https://leetcode.com/problems/jewels-and-stones)

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

```
Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
```

<!--more-->

# 分析
水题，通过set就可以解决。
主要是C++的熟悉，如何通过vector来初始化一个set；
还有优雅的遍历String

# 代码
空间复杂度O(N),时间复杂度O(N)
```C++
class Solution {
public:
    int numJewelsInStones(string J, string S) {
        int res = 0;
        unordered_set<char> setJ(J.begin(), J.end());
        for (char s : S) if (setJ.count(s)) res++;
        return res;
    }
};
```
            