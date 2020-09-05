import math

def cmn_div(n):
    divs = []
    for i in range(1, int(math.sqrt(n)+1)):
        if n % i == 0:
            divs.append(i)
            if not i*i == n:
                divs.append(n//i)
    return sum(sorted(divs)[:-1])

res = []
for i in range(2, 10000):
    t = cmn_div(i)
    if i == cmn_div(t) and not i == t:
        print(i, t)
        res.append(i)

print(f"Sum: {sum(res)}")