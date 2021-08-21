my_list = [7, 5, 3, 3, 2]

while True:
    try:
        print(f"Рейтинг = {my_list}")
        rate = int(input("Введите новый рейтинг >>> "))
        rate_count = my_list.count(rate)

        if rate_count:
            index = my_list.index(rate) + rate_count
            my_list.insert(index, rate)
        else:
            if rate > my_list[0]:
                my_list.insert(0, rate)
            elif rate < my_list[-1]:
                my_list.append(rate)
            else:
                for id, rating in enumerate(my_list):
                    if rating < rate:
                        my_list.insert(id, rate)
                        break

        print(my_list)
    except ValueError:
        print("Неверное число")
    except KeyboardInterrupt:
        exit()