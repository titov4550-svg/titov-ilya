def find_common_participants(string_1, string_2, split=","):  # TODO Напишите функцию find_common_participants
    list_1 = string_1.split(split)
    list_2 = string_2.split(split)
    names = []
    for _, item_1 in enumerate(list_1):
        for _, item_2 in enumerate(list_2):
            if item_1 == item_2:
                names.append(item_1)
    return  sorted(names)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))# TODO Провеьте работу функции с разделителем отличным от запятой