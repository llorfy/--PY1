money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

all_money = money_capital
while all_money >= spend:
    all_money -= spend
    spend += spend * increase
    all_money += salary
    month += 1

print(month)
