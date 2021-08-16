enter = int(input("Введите число >>> "))

number = enter
max = 0

while number and max != 9:
    print(number)
    current = number % 10
    number = number // 10
    max = current if current > max else max

print(max)