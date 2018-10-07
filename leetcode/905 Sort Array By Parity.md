# 题目描述
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

```
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
```

<!--more-->

# 分析
题目的本意是:重新排列这个数组，让偶数排在前面

这个是可以在线操作的，时间复杂度是O(n)，空间复杂度是O(1).

# 代码
```C++
class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        int len = A.size();
        int left = 0;
        int right = len-1;
        while(left<right){
            if(A[left]%2==1 && A[right]%2==0){
                int temp = A[left];
                A[left] = A[right];
                A[right] = temp;
            }
            while(A[left]%2==0){
                left++;
            }
            while(A[right]%2==1){
                right--;
            }
        }
        return A;
    }
};
```