cijferICOR = 8
cijferPROG = 7
cijferCSN = 7
gemiddelde = (cijferCSN,  cijferICOR, cijferCSN)
BeloningPerPunt = 30
gemiddeldecijfer = sum(gemiddelde)/len(gemiddelde)
print( "gemiddeld cijfer:", round(sum(gemiddelde)/(len(gemiddelde) ), 1))
print("verdient geld:", sum(gemiddelde) * BeloningPerPunt)
