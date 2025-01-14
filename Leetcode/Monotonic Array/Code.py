class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 0:
            return True
        f = nums[0]
        l = nums[n-1]
        if f>l:
            for k in range(n-1):
                if nums[k] < nums[k+1]:
                    return False
        elif f == l:
            for k in range(n-1):
                if nums[k]!=nums[k+1]:
                    return False
        else:
            for k in range(n-1):
                if nums[k]>nums[k+1]:
                    return False
        return True
        

