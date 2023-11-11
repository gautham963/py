#Leet Code problem 1672, to fine the customer with the maximum wealth. 
from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        Wealth = []
        for values in accounts:
            TotalWealth = 0
            for money in values:
                TotalWealth += int(money)
            Wealth.append(TotalWealth)

        maxWealth = max(Wealth)
        return maxWealth

solver = Solution()
number_of_accounts = int(input("Enter the number of accounts: "))
input_accounts = [(input('Enter the number: ').split())for _ in range(number_of_accounts)]
output = solver.maximumWealth(input_accounts)
print(output)
