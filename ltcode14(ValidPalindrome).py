#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s).lower()
        s = list([val for val in s if val.isalnum()])
        s = "".join(s)
        s1 = s[::-1]
        if s1 == s:
            return True
        else:
            return False
