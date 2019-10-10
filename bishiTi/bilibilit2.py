import  sys
year,month,day = map(int,sys.stdin.readline().split('-'))

# use month
day += (month -1) * 30
if month < 9:
    day += month//2
else:
    day += (month +1)//2
# 闰年
if month > 2:
    if year %400 ==0 or year %4== 0 and year %100 !=0 :
        day -= 1
    else:
        day -= 2
print(day)
