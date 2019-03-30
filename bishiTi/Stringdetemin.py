'''
Given a string s and a dictionary of words dict,
add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences.

s ="catsanddog"
dict ="cat", "cats", "and", "sand", "dog"
'''

'''
思路： 回溯法
'''
class Solution:
    def splitWord(self,s,dictw):
        ifFinished=False
        result =[]
        index1 = 0
        index2 = 0
        j = 0
        while True:
            if s[index1:index2] in dictw:
                index1