def smallest_multiple():
    import math
    res = 1
    for i in range(10, 21):
        res *= i // math.gcd(i, res)
    return res

if __name__ == "__main__":
    n = smallest_multiple()
    print(n)