# 题目描述

[原题链接](https://leetcode.com/problems/fair-candy-swap/description/)

Alice and Bob have candy bars of different sizes: A[i] is the size of the i-th bar of candy that Alice has, and B[j] is the size of the j-th bar of candy that Bob has.

Since they are friends, they would like to exchange one candy bar each so that after the exchange, they both have the same total amount of candy.  (The total amount of candy a person has is the sum of the sizes of candy bars they have.)

Return an integer array ans where ans[0] is the size of the candy bar that Alice must exchange, and ans[1] is the size of the candy bar that Bob must exchange.

If there are multiple answers, you may return any one of them.  It is guaranteed an answer exists.
```
Input: A = [1,1], B = [2,2]
Output: [1,2]

Input: A = [1,2], B = [2,3]
Output: [1,2]

Input: A = [2], B = [1,3]
Output: [2,3]

Input: A = [1,2,5], B = [2,4]
Output: [5,4]
```

<!--more-->

# 分析
可以分析出，如果A选择一个元素出来需要交换，那么B中需要交换的元素是固定的。

所以只需要在B中寻找，是否存在这个固定的元素即可。

具体查找的工作，可以通过二分查找，set来实现。

# 代码
空间复杂度O(N),时间复杂度O(N)
```C++
class Solution {
public:
    vector<int> fairCandySwap(vector<int>& A, vector<int>& B) {
        int A_totle = 0;
        int A_len = A.size();
        for(int i=0;i<A_len;i++){
            A_totle+=A[i];
        }
        int B_totle = 0;
        int B_len = B.size();
        for(int i=0;i<B_len;i++){
            B_totle+=B[i];
        }
        int A_B_mean = (A_totle + B_totle) /2;
        int B_give_A_give = A_B_mean - A_totle;
        std::set<int> B_set(B.begin(),B.end());
        for(int i=0;i<A_len;i++){
            int search_key = A[i] + B_give_A_give;
            if(B_set.find(search_key) != B_set.end()){
                vector<int> ans;
                ans.push_back(A[i]);
                ans.push_back(search_key);
                return ans;
            }
        } 
    }
};
```
