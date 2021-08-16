enter = int(input("Введите время в секундах:"))

only_seconds = enter

hours = only_seconds // 3600
minutes = (only_seconds % 3600) // 60
seconds = (only_seconds % 3600) % 60


print(f"{hours:>02}:{minutes:>02}:{seconds:>02}")