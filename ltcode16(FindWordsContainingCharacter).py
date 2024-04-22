#You are given a 0-indexed array of strings words and a character x.

#Return an array of indices representing the words that contain the character x.

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        List = []
        for i in range(len(words)):
            if x in words[i]:
                List.append(i)

        return List
