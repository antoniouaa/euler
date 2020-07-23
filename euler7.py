import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1, 1):
        if not n % i:
            return False
    return True

if __name__ == "__main__":
    counter = 0
    num = 2
    while not counter == 10000:
        num += 1
        if is_prime(num):
            counter += 1
        
    print(num)