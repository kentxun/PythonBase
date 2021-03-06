'''
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

'''

'''
同样的，递归就是压栈压栈压栈，出栈出栈出栈的过程，我们可以利用动态规划的思想，省略压栈的过程，直接从 bottom 到 top。

用一个 dp 数组， dp [ i ] 代表字符串 s [ i, s.len-1 ]，也就是 s 从 i 开始到结尾的字符串的解码方式。

这样和递归完全一样的递推式。

如果 s [ i ] 和 s [ i + 1 ] 组成的数字小于等于 26，那么

dp [ i ] = dp[ i + 1 ] + dp [ i + 2 ]

public int numDecodings(String s) {
    int len = s.length();
    int[] dp = new int[len + 1];
    dp[len] = 1; //将递归法的结束条件初始化为 1 
    //最后一个数字不等于 0 就初始化为 1
    if (s.charAt(len - 1) != '0') {
        dp[len - 1] = 1;
    }
    for (int i = len - 2; i >= 0; i--) {
        //当前数字时 0 ，直接跳过，0 不代表任何字母
        if (s.charAt(i) == '0') {
            continue;
        }
        int ans1 = dp[i + 1];
        //判断两个字母组成的数字是否小于等于 26
        int ans2 = 0;
        int ten = (s.charAt(i) - '0') * 10;
        int one = s.charAt(i + 1) - '0';
        if (ten + one <= 26) {
            ans2 = dp[i + 2];
        }
        dp[i] = ans1 + ans2;

    }
    return dp[0];
}
'''
class Solution:
    def numDecodings(self,s):
        length = len(s)
        dp = [0 for _ in range(length+1)]
        dp[length] = 1
        if s[length-1]!='0':
            dp[length-1] = 1
        for i in range(length-2,-1,-1):
            if s[i] == 0:
                continue
            ans1 = dp[i+1]
            ans2 = 0
            ten  = (s[i]-'0')*10
            one = s[i+1]-'0'
            if ten+one <= 26:
                ans2 = dp[i+2]
            dp[i] =ans1 + ans2
        return  dp[0]