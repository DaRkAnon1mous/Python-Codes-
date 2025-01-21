class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def help(i,subset):
            if i == len(nums):
                res.append(subset[:])
                return
            ## include
            subset.append(nums[i])
            help(i+1,subset)
            subset.pop()

            ## exclude
            while i < len(nums)-1 and nums[i]==nums[i+1]:
                i+=1
            help(i+1,subset)
        help(0,[])
        return res
