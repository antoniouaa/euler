from euler7 import is_prime

if __name__ == "__main__":
    res = 0
    for i in range(2, 2000000):
        if is_prime(i):
            res += i 
            
    print(res)