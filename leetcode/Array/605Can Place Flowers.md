
# 题目描述
[原题链接](https://leetcode.com/problems/can-place-flowers/)

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

```
Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
```

<!--more-->

# 分析
水题，只需要一遍扫描即可。就是如果左右，和自己都是空的就可以栽种

# 代码
空间复杂度O(1),时间复杂度O(n)
```C++
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int len = flowerbed.size();
        int count = 0;
        if(flowerbed[0]==0 && flowerbed[1]==0){
            count++;
            flowerbed[0] = 1;
        }
        for(int i=1;i<len-1;i++){
            if(flowerbed[i]==0 && flowerbed[i-1]==0 && flowerbed[i+1] == 0){
                count++;
                flowerbed[i] = 1;
            }
        }
        if(flowerbed[len-1]==0 && flowerbed[len-2]==0){
            count++;
            flowerbed[len-1] = 1;
        }
        if(count>=n){
            return true;
        }else{
            return false;
        }
    }
};
```
            