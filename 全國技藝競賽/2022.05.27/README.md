# TODO LIST

- [x] 1試題一：四則運算直譯器  
- [ ] 2試題二：數值轉換程式  
  - [十进制小数转化为二进制小数](https://www.runoob.com/w3cnote/decimal-decimals-are-converted-to-binary-fractions.html)
- [X] 3試題三：排列組合  
  - [itertools.permutations(iterable, r=None)](https://docs.python.org/zh-tw/3.9/library/itertools.html#itertools.permutations)
- [X] 4試題四：長整數加法計算  
- [ ] 5試題五：正整數分割  
- [X] 6試題六：計算1的數目  
- [X] 7試題七：費氏級數  
  - `1 1 2 3 5 8 13 21 34 55 89 144 233 377 610...`
  - ```py
    def fib(n): return n if n < 2 else fib(n-1) + fib(n-2)
    ```
- [ ] 8試題八：數列  
- [X] Problem1：找出文章中使用的英文單字字數  
- [ ] Q101：The Block Problem  

---

## sth

- [functools.reduce(function, iterable[, initializer])](https://docs.python.org/zh-tw/3.9/library/functools.html#functools.reduce)

```py
with open(file='./input.txt', mode='r', encoding='utf8') as rfile:
    ...

with open(file='./output.txt', mode='w', encoding='utf8') as wfile:
    ...
```
