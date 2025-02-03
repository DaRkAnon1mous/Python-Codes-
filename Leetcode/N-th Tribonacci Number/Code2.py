## Memoization Approach  (Time Limit Exceed):
class Solution:
    def tribonacci(self, n: int) -> int:
        arr= {0:0,1:1,2:1}
        if n in arr:
            return arr[n]
        else:
            arr[n]=self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
            return arr[n]
