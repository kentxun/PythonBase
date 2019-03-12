'''
请编写一个方法，将字符串中的空格全部替换为“%20”。
假定该字符串有足够的空间存放新增的字符，并且知道字符串的真实长度(小于等于1000)，
同时保证字符串由大小写的英文字母组成。
给定一个string iniString 为原始的串，以及串的长度 int len, 返回替换后的string。

测试样例：
"Mr John Smith”,13
返回："Mr%20John%20Smith"
”Hello  World”,12
返回：”Hello%20%20World”
'''
# -*- coding:utf-8 -*-

class Replacement:
    def replaceSpace(self, iniString, length):
        # write code here
        spaceCount = 0
        for i in iniString:
            if i == ' ':
                spaceCount+=1
        OutString = list(iniString+' '*spaceCount*3)
        index = 0
        space =0
        while  index <= length and space <= spaceCount:
            if iniString[index]==' ':
                OutString[index+space*3] = '%'
                OutString[index+1+space*3] = '2'
                OutString[index+2+space*3] = '0'
                index +=1
                space +=1
            else:
                OutString[index+space*3]=iniString[index]

        return ''.join(OutString)

class Replacement0:
    def replaceSpace(self, iniString, length):
        # write code here
        spaceCount = 0
        OutString=[]
        for t  in iniString:
            if t == ' ':
               OutString.append('%')
               OutString.append('2')
               OutString.append('0')
            else:
                OutString.append(t)
        return ''.join(OutString)


# -*- coding:utf-8 -*-
class Replacement1:
    def replaceSpace(self, iniString, length):
        # write code here
        return '%20'.join(iniString.split(' '))


class Replacement2:
    def replaceSpace(self, iniString, length):
        # write code here

        return iniString.replace(' ', '%20')