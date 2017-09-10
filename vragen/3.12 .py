def nega(*numlist):
    for num in numlist:
        if num < 0:
            print(num)
print(nega(5, 0, -2))