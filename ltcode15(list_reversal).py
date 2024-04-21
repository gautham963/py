#Write a function that reverses a string. The input string is given as an array of characters s.

#You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        #s.reverse() This is one method

        #this is the other method with the logic.
        for i in range(len(s)//2):#This is so that the loop only iterates to half the length
            s[i],s[-i-1] = s[-i-1],s[i] #The i will get the first character, -i-1 is used to get the last character               
        print(s)
