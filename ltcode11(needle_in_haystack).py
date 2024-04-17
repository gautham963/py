#Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            i = needle[0]
            ii = haystack.index(needle)
            return ii
        
        elif needle not in haystack:
            return -1
