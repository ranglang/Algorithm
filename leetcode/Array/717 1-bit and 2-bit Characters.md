# 题目描述

[原题链接](https://leetcode.com/problems/contains-duplicate/)

We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.
```
Input: 
bits = [1, 0, 0]
Output: True
Explanation: 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.

Input: 
bits = [1, 1, 1, 0]
Output: False
Explanation: 
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
```

<!--more-->

# 分析
我看到题目用了一个比较蠢的办法，递归的向前推导。是反过来考虑的

其实可以从前向后考虑，如果是0，肯定是一位，如果是1，肯定是2位。这样就可以看看最后是不是正常的了。


# 代码
空间复杂度O(n),时间复杂度O(n)
```C++
class Solution {
public:
    bool isOneBitCharacter(vector<int>& bits) {
        vector<int> sub(bits.begin(),bits.end()-1);
        return isCanDecode(sub); 
    }
    bool isCanDecode(vector<int>& bits){
        int length = bits.size();
        if(length==0){
            return true;
        }
        if(length==1){
            if(bits[0] == 0){
                return true;
            }else{
                return false;
            }
        }
        if(length==2){
            if(bits[0]==0 && bits[1] == 1){
                return false;
            }else{
                return true;
            }
        }
        if(bits[length-1]==0){
            vector<int> sub_1(bits.begin(),bits.end()-1);
            bool option_1 = isCanDecode(sub_1);
            bool option_2 = true;
            if(bits[length-2]==1){
                vector<int> sub_2(bits.begin(),bits.end()-2);
                option_2 = isCanDecode(sub_2);
            }
            return option_1 || option_2;
        }else{
            if(bits[length-2]==1){
                vector<int> sub_3(bits.begin(),bits.end()-2);
                return isCanDecode(sub_3);
            }else{
                return false;
            }
        }
        
    }
};
```


空间复杂度O(1),时间复杂度O(n)
```C++
class Solution {
public:
    bool isOneBitCharacter(vector<int>& bits) {
        int length = bits.size();
        int i=0;
        for(;i<length-1;){
            if(bits[i]==0){
                i++;
            }else{
                i+=2;
            }
        }
        if(i==length-1){
            return true;
        }else{
            return false;
        }
    }
};
```
