## Approach 1 (O nlogn)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        s=0
        h= []
        for i in range(len(nums)):
            s = nums[i]*nums[i]
            h.append(s)
        h = sorted(h)
        return(h)

## Approach 2 (O n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n  # To store the sorted squares
        left, right = 0, n - 1
        pos = n - 1  # Position to fill in the result array (starting from the end)
    
        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2
            if left_square > right_square:
                result[pos] = left_square
                left += 1
            else:
                result[pos] = right_square
                right -= 1
            pos -= 1
    
        return result
