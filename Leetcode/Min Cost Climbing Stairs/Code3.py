
## Best Time optimized code
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

    # each element in the array will be the cost of reaching that index, not cost of using
        arr = [-1] * (n + 1)
    # as you can start at step with index 0 or 1
        arr[0] = 0
        arr[1] = 0
        for i in range(2, n + 1):
            prevOne = cost[i - 1] + arr[i - 1]
            prevTwo = cost[i - 2] + arr[i - 2]
            arr[i] = min(prevOne, prevTwo)
        return arr[n]
