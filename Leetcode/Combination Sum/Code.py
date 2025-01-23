class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        def help(i,comb,sumt):
            if sumt > target:
                return
            if sumt == target:
                res.append(comb[:])
                return
            for j in range(i,n):
                comb.append(candidates[j])
                help(j,comb,sumt +candidates[j])
                comb.pop()
        help(0,[],0)
        return res
