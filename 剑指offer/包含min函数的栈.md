---
title: 剑指offer-包含min函数的栈
date: 2018-05-03 13:36:02
categories: 剑指offer
tags: 
 - 栈
---

# 题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。


<!--more-->

# 分析
通过两个堆栈实现，一个是正常堆栈，另一个用来记录依次入栈的最小值.

比如，data中依次入栈，

5,  4,  3, 8, 10, 11, 12, 1

则min依次入栈，

5,  4,  3，no,no, no, no, 1

no代表此次不如栈

每次入栈的时候，如果入栈的元素比min中的栈顶元素小或等于则入栈，否则不如栈。

# 代码
```C++
class Solution {
public:
    stack<int> s;
    stack<int> min_s;
    void push(int value) {
        s.push(value);
        if(min_s.empty() || value<= min_s.top() ){
            min_s.push(value);
        }
    }
    void pop() {
        if(s.top()==min_s.top()){
            s.pop();
            min_s.pop();
        }else{
            s.pop();
        }
    }
    int top() {
        return s.top();
    }
    int min() {
        return min_s.top();
    }
};
```