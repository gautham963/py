#Given an array of strings words and a string s, determine if s is an acronym of words.

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        char = ''
        for i in range(len(words)):
            char += words[i][0]

        if s == char:
            return True
        else:
            return False
