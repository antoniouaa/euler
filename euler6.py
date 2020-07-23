def sum_square_diff(n=100):
    sq = [i**2 for i in range(1, n+1)]
    return sum(range(1, n+1))**2 - sum(sq)

if __name__ == "__main__":
    res = sum_square_diff(100)
    print(res)