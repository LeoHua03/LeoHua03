favorite_places={
    'Leo':['HK','UK'],
    'Linda':['UK','Japan'],
    'Danny':['USA','Korea','India'],
    }
print(f"I know some friends who like these places:")
for people,places in favorite_places.items():
    print(f"{people} like the following countries:")
    for place in places:
        print(f"\t{place}")