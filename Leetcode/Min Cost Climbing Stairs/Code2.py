## Memoization Approach No time limit exceed
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

    # helper(index) will return the min cost of reaching the top starting at index which
    # means using the step at index
        array = [-1] * n

        def helper(index):
            if index >= n:
                return 0
            if array[index] != -1:
                return array[index]
            # climb one
            one = cost[index] + helper(index + 1)
            # climb two
            two = cost[index] + helper(index + 2)
            array[index] = min(one, two)
            return array[index]

        return min(helper(0), helper(1))
