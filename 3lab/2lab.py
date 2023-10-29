# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group,participants_second_group,argument=','):
    participants_first_group=list(set(participants_first_group.split(argument)))
    participants_second_group=list(set(participants_second_group.split(argument)))
    ksfm=set(participants_first_group).intersection(participants_second_group)
    return list(ksfm)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group,participants_second_group,'|'))


# TODO Провеьте работу функции с разделителем отличным от запятой
