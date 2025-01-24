class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()

        def backtrack(index, currSum, curr):
            if currSum == target:
                res.append(curr[:])
                return
            if currSum > target:
                return
            if index > len(candidates) - 1:
                return
            hash = {}
            for j in range(index, len(candidates)):
                if candidates[j] not in hash:
                    hash[candidates[j]] = 1
                    curr.append(candidates[j])
                    backtrack(j + 1, currSum + candidates[j], curr)
                    curr.pop()

        backtrack(0, 0, [])
        return res
