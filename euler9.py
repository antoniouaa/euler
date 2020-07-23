def pyth_triplet():
    for i in range(1, 1000):
        for j in range(i, 1000):
            k = 1000 - i - j
            if i**2 + j**2 == k**2:
                return i, j, k
            
if __name__ == "__main__":
    tupl = pyth_triplet()
    print(tupl)
    print(tupl[0]*tupl[1]*tupl[2])