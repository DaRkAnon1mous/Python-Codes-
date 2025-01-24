class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtrack(number,curr,currSum):
            if currSum ==n and len(curr)==k:
                res.append(curr[:])
                return
            if currSum >n or len(curr)==k:
                return
            for x in range(number,10):
                curr.append(x)
                backtrack(x+1,curr,currSum+x)
                curr.pop()
        backtrack(1,[],0)
        return res      
