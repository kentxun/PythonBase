class InsertionSort:
    def insertionSort(self, A, n):
        for i in range(1,n):
            for j in range(i):
                if A[i] > A[j]:
                    A[i],A[j]=A[j],A[i]
        return A
import sys
args = sys.stdin.readline()
args = eval(args)
Listin = args[0]
N = args[1]

a = InsertionSort()
out = a.insertionSort(Listin,len(Listin))
print(out[:N])