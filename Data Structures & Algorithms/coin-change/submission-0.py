class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {i: amount+1 for i in range(amount+1)}
        memo[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                subproblem = i - c
                if subproblem < 0:
                    continue
            
                memo[i] = min(memo[i], 1+memo[subproblem])
                
        
        return memo[amount] if memo[amount] != amount+1 else -1