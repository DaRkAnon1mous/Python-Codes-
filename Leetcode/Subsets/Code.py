class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def help(i,nums,subset):
            if i == n:
                res.append(subset.copy())
                return
            help(i+1,nums,subset)
            subset.append(nums[i])
            help(i+1,nums,subset)
            subset.pop()
        help(0,nums,[])
        return res
