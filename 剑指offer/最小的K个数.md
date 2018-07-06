---
title: 剑指offer-最小的K个数
date: 2018-07-06 21:36:02
categories: 剑指offer
tags: 
 - 优先队列
---

# 题目描述
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

<!--more-->

# 分析
第一反应就是先排序然后取出前k个数就行，不过这样的效率是Olog(n)

然后可以采用优先队列的方式，里面始终只有k个数字进行排序，效率是Olog(k)

不过注意的是边界条件的思考，k是可能小于0的。

# 代码
排序
```C++
class Solution {
public:
    vector<int> GetLeastNumbers_Solution(vector<int> input, int k) {
        int length = input.size();
        if(k>length){
            vector<int> result;
            return result;
        }
        sort(input.begin(),input.end());
        vector<int> result(input.begin(),input.begin()+k);
        return result;
    }
};
```

优先队列
```C++
class Solution {
public:
    vector<int> GetLeastNumbers_Solution(vector<int> input, int k) {
        int length = input.size();
        vector<int> result;
        if(k>length || k <= 0){
            return result;
        }
        priority_queue<int> pq;
        for(int i=0;i<k;i++){
            pq.push(input[i]);
        }
        for(int i=k;i<length;i++){
            if(input[i]<pq.top()){
                pq.pop();
                pq.push(input[i]);
            }
        }
        for(int i=0;i<k;i++){
            result.push_back(pq.top());
            pq.pop();
        }
        return result;
    }
};
```
