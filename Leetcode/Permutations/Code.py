class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def help(i):
            if i == n-1 :
                res.append(nums[:])
                return
            for j in range(i,n):
                nums[i],nums[j]=nums[j],nums[i]
                help(i+1)
                nums[i],nums[j]=nums[j],nums[i]
        help(0)
        return res    
        
        
