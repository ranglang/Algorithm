# 题目描述

[原题链接](https://leetcode.com/problems/monotonic-array/description/)

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.


```
Input: [1,2,2,3]
Output: true

Input: [6,5,4,4]
Output: true

Input: [1,3,2]
Output: false

Input: [1,2,4,5]
Output: true

Input: [1,1,1]
Output: true
```

<!--more-->

# 分析
原先的想法比较复杂，首先需要判断出这个是增长还是下降，确定以后检查是否都满足这个要求。

后来其实有非常简洁的方案，就是预定义好两个可能，增长/下降，遍历只要有一个不满足，就直接将对应的可能去除。最后检查是不是还有可能存在。

# 代码
空间复杂度O(1),时间复杂度O(N)
```C++
class Solution {
public:
    bool isMonotonic(vector<int>& A) {
        int len = A.size();
        if(len<=2){
            return true;
        }
        bool is_first = true;
        int  direction = 0;
        for(int i=1;i<len;i++){
            int distance = A[i]-A[i-1];
            if(distance==0){
                continue;
            }
            if(is_first){
                is_first = false;
                direction = distance;
            }else{
                if(direction > 0 != distance > 0){
                    return false;
                }
            }
            
        }
        return true;
    }
};
```

空间复杂度O(1),时间复杂度O(N)
```C++
class Solution {
public:
    bool isMonotonic(vector<int>& A) {
        int len = A.size();
        if(len<=2){
            return true;
        }
        bool increasing = true;
        bool decreasing = true;
        for(int i=1;i<len;i++){
            if(A[i]>A[i-1]) decreasing = false;
            if(A[i]<A[i-1]) increasing = false;
        }
        return increasing || decreasing;
    }
};
```

