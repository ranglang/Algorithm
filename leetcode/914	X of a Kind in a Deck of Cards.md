
# 题目描述
[原题链接](https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/)

In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.

```
Example 1:

Input: [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]
Example 2:

Input: [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.
Example 3:

Input: [1]
Output: false
Explanation: No possible partition.
Example 4:

Input: [1,1]
Output: true
Explanation: Possible partition [1,1]
Example 5:

Input: [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2]
```

<!--more-->

# 分析
主要是实现一个counter的功能。然后就是找到一列数字的最大公约数。


# 代码
空间复杂度O(n),时间复杂度O(n)
```C++
class Solution {
public:
    bool hasGroupsSizeX(vector<int>& deck) {
        map<int,int> num_count;
        int len = deck.size();
        for(int i=0;i<len;i++){
            if(num_count.find(deck[i])==num_count.end()){
                num_count[deck[i]] = 1;
            }else{
                num_count[deck[i]] += 1;
            }
        }
        map<int,int>::iterator it;
        vector<int> count;
        for(it=num_count.begin();it!=num_count.end();it++){
            count.push_back(it->second);
        }
        sort(count.begin(),count.end());
        if(count.size()==1){
            if(count[0]>=2){
                return true;
            }else{
                return false;
            }
        }
        int min_divisor = 0;
        for(int i=2;i<=count[0];i++){
            if(count[0]%i==0 && count[1]%i==0){
                min_divisor = i;
                break;
            }
        }
        if(min_divisor==0){
            return false;
        }
        for(int i=2;i<count.size();i++){
            if(count[i]%min_divisor!=0){
                return false;
            }
        }
        return true;
    }
};
```
            