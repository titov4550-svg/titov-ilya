months = 0
money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

while money_capital + salary >= spend:
    spend += spend * increase
    money_capital -= spend - salary
    months += 1

print("Количество месяцев, которое можно протянуть без долгов:", months)