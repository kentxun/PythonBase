'''
ans = 0;
cin >> l;
for (int i = 1; i < l / 3; i++) {
    for (int j = i; j < l / 2; j++) {
        int k = l - i - j;
        if (i * i + j * j == k * k) {
            ans++;
        }
    }
}
'''

import  sys
res  = 0
l = int(sys.stdin.readline().strip())
for i in range(1,int(l/3)):
   for j in range(i,int(l/2)):
       k = l - i - j
       if i*i + j*j == k*k:
           res+=1
print(res)
