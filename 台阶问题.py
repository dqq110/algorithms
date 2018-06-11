#共有n个台阶，每次只能上1个台阶或者2个台阶，共有多少种方法爬完台阶。
#f(n)表示走完n个台阶的方法

#递归写法,这个效率最低
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return f(n-1) + f(n-2)

#迭代写法,也叫循环写法
def f1(n):
    res = [0 for i in range(n+1)]
    res[1] = 1
    res[2] = 2
    for i in range(3,n+1):
        res[i] = res[i-1] + res[i-2]
    return res[n]
print(f1(4))

#使用缓存写法
cache = {}
def fib(n):
    if n not in cache.keys():
        cache[n] = _fib(n)
        return cache[n]

def _fib(n):
    if n == 1 or n == 2:
        return n
    else:
        return fib(n-1) + fib(n-2)