months = int(input("Укажите месяц рождения: "))
part_year = {
    "winter": (1, 2, 12),
    "spring": (3, 4, 5),
    "summer": (6, 7, 8),
    "autumn": (9, 10, 11),
}
for season, month in part_year.items():
    if months in month:
        print(f"Время года: {season}")
        break
