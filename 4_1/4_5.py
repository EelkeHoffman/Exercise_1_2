#lijst = list(input("cijfers: "))

test = []
def kwadraten_som(a):
    for z in a:
        if z > 0:
            test.append(z * z)
    return sum(test)




print(kwadraten_som(a = [3, 4]))
