'''
每个孩子都有一个满足度，每个饼干都有一个大小，只有饼干的大小大于等于一个孩子的满足度，
该孩子才会获得满足。求解最多可以获得满足的孩子数量。

Input: [1,2], [1,2,3]
Output: 2

Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2.
You have 3 cookies and their sizes are big enough to gratify all of the children,
You need to output 2.
'''

class CookieAssign:
    def findContentChildren(self,child,cookie):
        child.sort()
        cookie.sort()
        gi,si=0,0
        while gi<len(child) and si < len(cookie):
            if child[gi] <= cookie[si]:
                gi += 1
            else:
                si += 1
        return gi