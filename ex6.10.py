favorite_numbers={
    'a':['1','5'],
    'b':['2','4'],
    'c':['1','2','8','9'],
}
for people,numbers in favorite_numbers.items():
    print(f"{people} likes the following numbers:")
    for number in numbers:
        print(f"\t{number}")