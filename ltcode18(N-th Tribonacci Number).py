#The Tribonacci sequence Tn is defined as follows: 

#T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

#Given n, return the value of Tn.

class Solution:
    def tribonacci(self, n: int) -> int:
        vals =[]
        if n == 1:
            vals.append(n)
        else:
            for i in range(n):
                if i == 0:
                    vals.append(i)
                elif i == 1:
                    vals.append(i)
                elif i > 1:
                    val = sum(vals)
                    vals.append(val)
                    if len(vals) > 3:
                        vals.pop(0)

        return sum(vals)
        
