def palindromic_num():
    largest = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            num = i * j
            if str(num) == str(num)[::-1]:
                largest.append(num)
    return largest

num = sorted(palindromic_num())[-1]
print(num)