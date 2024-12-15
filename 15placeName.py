def COUNTNOW(PLACES):
    for place in PLACES:
        if len(place) > 7:
            print(place)

PLACES = ["SYDNEY", "TOKYO", "PINKCITY", "BEIJING", "SUNCITY"]
COUNTNOW(PLACES)
