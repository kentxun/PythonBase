'''
将一个字符串中的空格替换成 "%20"。

Input:
"A B"

Output:
"A%20B"
'''
def f(n):
    if n<=2 :
        return 1
    return  f(n-1)+f(n-2)

print(f(12))