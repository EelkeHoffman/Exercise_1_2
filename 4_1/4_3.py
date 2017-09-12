lengte = int((input("hoe lang ben je in cm?")))
def lang_genoeg(lengte):
    if lengte > 120:
        print("lang genoeg")
    else:
        print("helaas")
lang_genoeg(lengte)