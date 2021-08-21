words = input("Слова через пробел: ").split()

for number, symbols in enumerate(words, start=1):
    print(f"{number}. {symbols[:10]}")
