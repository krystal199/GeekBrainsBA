revenue = int(input("Выручка: "))
costs = int(input("Издержки: "))

profit = revenue - costs

if profit:
    profitability = profit / revenue
    print("Прибыль=", profit, "Рентабельность=", profitability)

    employees = int(input("Численность сотрудников:"))

    profit_of_employees = profit / employees
    print("Прибыль на одного сотрудника =", profit_of_employees)
else:
    print("Убыток=", profit)