# using of boolean values for weather recommendationS
print("*" * 10)
print("Weather Recommendation")
print("*" * 10)

is_hot = False
is_cold = False
is_rainy = True
is_sunny = False
is_snowy = False
is_foggy = False
is_cloudy = False
is_overcast = False
is_clear = False
is_partly_cloudy = False
is_mostly_cloudy = False

if is_hot:
    print("It's hot!, Make sure to drink some water")
elif is_cold:
    print("It's cold!, Make sure to wear warm clothes")
elif is_rainy:
    print("It's rainy!, Make sure to Take an Umbrella")
elif is_cloudy:
    print("It's cloudy!, It may rain soon")
elif is_sunny:
    print("It's sunny!, Use Sunscreen")
elif is_snowy:
    print("It's snowy!, Don't go outside")
elif is_foggy:
    print("It's foggy!, Used dipper on Car")
elif is_overcast:
    print("It's overcast!, Don't go outside")
elif is_clear:
    print("It's clear!, Seems to be a Beautiful Day")
elif is_partly_cloudy:
    print("It's partly cloudy, Seems to be a Beautiful Day")
elif is_mostly_cloudy:
    print("It's mostly cloudy, There are chances of rain today")
else:
    print("Weather is not working right now")

print("Enjoy your Day!")