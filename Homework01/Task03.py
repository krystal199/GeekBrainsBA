n = int(input("Введите число >>> "))

number = n
count = 0
nn = number

while nn:
    nn //= 10
    count += 1

row_one = (10 ** count) + 1
row_two = (10 ** (count * 2)) + row_one

result = number + (number * row_one) + (number * row_two)

print(result)