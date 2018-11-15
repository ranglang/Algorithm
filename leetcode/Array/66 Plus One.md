# 题目描述

[原题链接](https://leetcode.com/problems/remove-element/)

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

```
Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
```

<!--more-->

# 分析
水题，一个递归的过程，需要重点考虑第一位。

# 代码
空间复杂度O(1),时间复杂度O(n)
```C++
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int length = digits.size();
        for(int i=length-1;i>=0;){
            digits[i] = digits[i] + 1;
            if(digits[i] <=9){
                break;
            }else{
                digits[i] %= 10;
                i--;
            }
        }
        if(digits[0] == 0){
            digits.insert(digits.begin(),1);
        }
        return digits;
    }
};
```
