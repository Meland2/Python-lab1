users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
dis={"Общее количество": 0, "Уникальные посещения": 0}
all_visit=len(users)
sets=len(set(users))
dis["Общее количество"]=all_visit
dis["Уникальные посещения"]=sets
print(dis)