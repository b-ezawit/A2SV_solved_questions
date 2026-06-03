class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        holding = float('-inf')
        notHolding = 0

        for price in prices:
            holding = max(holding, notHolding-price)
            notHolding = max(notHolding, price+holding-fee)
        
        return notHolding