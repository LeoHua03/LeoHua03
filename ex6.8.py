#goal    '誰‘’s pet is a ‘動物’
pet1={'cat':'Linda'}
pet2={'dog':'Leo'}
pet3={'rabbit':'Mike'}
pets=[pet1,pet2,pet3]

for pet_dict in pets:
    for pet,host in pet_dict.items():
        print(f"{host}'s pet is a {pet}")