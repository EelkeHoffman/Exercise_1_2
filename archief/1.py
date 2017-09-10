ingredients = ["flour", "sugar", "butter", "apples"]



def swap(test):
    res = test[0], test[(len(ingredients)- 1)]  = test[(len(ingredients)- 1)], test[0]
    test = res
    print(ingredients)


print(swap(ingredients))
