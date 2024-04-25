#A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

#You are given an array of strings sentences, where each sentences[i] represents a single sentence.

#Return the maximum number of words that appear in a single sentence.

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        lt = []
        for i,sentence in enumerate(sentences):
            words = sentence.split(' ')
            lt.append(len(words))

        return max(lt)
        
