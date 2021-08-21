features = {
    "Название": str,
    "Цена": int,
    "Количество": int,
    "Единица измерения": str,
}

product_list = []
product_counter = 1

while True:
    decision = input(f"Товаров = {len(product_list)}, добавить? [y/n] ").lower()

    if decision == 'n':
        break
    else:
        product_info = {}

        for property_name, property_type in features.items():
            user_input = input(f"Заполните поле '{property_name}' >>> ")
            product_info[property_name] = property_type(user_input)

        product_list.append((product_counter, product_info))
        product_counter += 1

product_analytics = {}

for analytics_key in features.keys():
    item_list = []

    for product in product_list:
        item_list.append(product[1][analytics_key])

    product_analytics[analytics_key] = set(item_list)

print(product_analytics)