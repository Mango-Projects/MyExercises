from sys import stdin
from statistics import (
    mean,       #平均數
    pvariance,  #變異數
    median,     #中位數
    mode        #眾數
    )

data = map(int, stdin.read().splitlines())
print(f'平均數：{mean()}\n變異數：{}\n中位數：{}\n眾　數：{}')