from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        count = [-1] * (amount + 1)
        for i in range(0, amount + 1) :
            if i == 0 :
                count[i] = 0
            elif i in coins :
                count[i] = 1
            else :
                m = 100000
                for j in coins :
                    if j > amount : continue
                    if i - j >= 1 :
                        if count[i - j] != -1 :
                            if m > count[i-j] :
                                m = count[i-j]
                if m != 100000 :
                    count[i] = m + 1

        return count[amount]