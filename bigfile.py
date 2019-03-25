import hashlib

def hash_file(filename):
   """该函数返回传入文件的SHA-1哈希值"""

   # 创建一个哈希对象
   h = hashlib.sha1()

   # 以二进制读取模式打开一个文件
   with open(filename,'rb') as file:

       # 循环直到文件结束
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # 返回摘要的十六进制表示
   return h.hexdigest()

def getText():
    txt=open('hamlet.txt','r').read()
    txt=txt.lower()
    for ch in "~@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
        txt=txt.replace(ch,' ')
    return txt

hamletTxt=getText()
words=hamletTxt.split()
counts={}
sumcount = 0
for word in words:
    counts[word]=counts.get(word,0)+1
    sumcount = sumcount + 1

dict_file={}
def read_file(file_path):
    with open(file_path,'rb') as file:
        txt=None
        for _ in range(1024):
            txt =file.read(1000000)
            txt = txt.lower()
            for ch in "~@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
                txt = txt.replace(ch, ' ')
            dict_file[_] = txt

dict_word={}
for k,v in dict_file:
    for key in v:
        if key in dict_word:
            dict_word[key]+=1
        else:
            dict_word[key]=1
if __name__ == '__main__':

    out = sorted(dict_word.items() , key=lambda items:items[1],reverse=True)


counts_ex = counts.copy()
for key in counts.keys():
    if key in excludes:
        counts_ex.pop(key)
items=list(counts_ex.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print('{0:<10}{1:>5}'.format(word,count))


class WordCount(object):
    def __init__(self)：
        pass

    def parse(self,line):
        return Count

# 划分1024个文件进行处理

# 每个文件大概10M