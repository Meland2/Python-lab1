money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
now_money=money_capital+salary # сколько денег есть на руках
count=0 # количество месяцев
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while now_money>spend:
    now_money+=-spend+salary
    spend+=spend*0.05
    count+=1
print("Количество месяцев, которое можно протянуть без долгов:", count)
