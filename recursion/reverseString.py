class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if s == []:
            return
        def helper(start,end,s):
            if start > end:
                return
            helper(start+1,end-1,s)
            s[start] ,s[end] = s[end],s[start]
        helper(0,len(s)-1,s)