a = int(input("КМ в первый день: "))
b = int(input("Цель: "))

day = 1

while a < b:
    day += 1
    a += a * .10
else:
    print("День достижения =", day)