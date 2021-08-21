s = input("Укажите числа через запятую : ").split(",")

z = len(s) - 1
for q in range(0, z, 2):
    index_a = q + 1
    s[q], s[index_a] = s[index_a], s[q]

print(s)
