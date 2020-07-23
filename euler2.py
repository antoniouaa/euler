from functools import reduce

fib = lambda n: reduce(lambda x,n:[x[1],x[0]+x[1]], range(n),[0,1])[0]

nums = [fib(i) for i in range(1, 34)]
evens = filter(lambda x: x&1==0, nums)
s = sum(evens)
print(s)