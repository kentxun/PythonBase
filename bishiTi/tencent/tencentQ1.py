# !/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
n = int(sys.stdin.readline().strip())
power =[int(i) for i in sys.stdin.readline().strip().split(' ')]
coin = [int(t) for t in sys.stdin.readline().strip().split(' ')]

# 性价比计算
value = []
for i in range(n):
    value.append(coin[i]/power[i])

value_max = coin[power.index(max(power))]/ max(power)
cost = 0
now_power = 0
monster = 0

while now_power < max(power):
    if now_power < power[monster]:
        now_power += power[monster]
        cost += coin[monster]
    else:
        if value[monster] >= value_max:
            now_power += power[monster]
            cost += coin[monster]
    monster += 1

print(cost)