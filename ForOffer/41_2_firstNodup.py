'''
请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。


一般思路：
dict记录，查询
'''

'''
提供一个高效的算法：
思路：时间复杂度O（1），空间复杂度O（n）
        1、用一个128大小的数组统计每个字符出现的次数
        2、用一个队列，如果第一次遇到ch字符，则插入队列；其他情况不在插入
        3、求解第一个出现的字符，判断队首元素是否只出现一次，如果是直接返回，否则删除继续第3步骤

分析：可以看出相同的字符只被插入一次，最多push128个，同时大多数情况会直接返回队首。所以大家不要被里面的while循环迷惑
'''
