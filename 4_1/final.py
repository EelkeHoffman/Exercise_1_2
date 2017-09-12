def standaardprijs(afstandKM):
    if afstandKM <= 0:
        return 0
    elif afstandKM >= 50:
        return 15 + (afstandKM * 0.6)
    else:
        return afstandKM * 0.6


def ritprijs(leeftijd, weekendrit, afstandKM):
    print(standaardprijs(afstandKM))
    if int(leeftijd) < 12 or int(leeftijd) >= 65:
        print(float(standaardprijs(int(afstandKM)) * 0.70))
    elif weekendrit is bool(True):
            print(float(standaardprijs(int(afstandKM)) * 0.60))
    else:
        print(standaardprijs(afstandKM))




ritprijs(int(input("leeftijd: ")), bool(True), int(input("afstand: ")))

# ritprijs(int(input("leeftijd: ")), bool(input("weekendrit")), int(input("afstand: "))) waarom werkt dit niet





# print(standaardprijs(int(input("kilometers:"))))
