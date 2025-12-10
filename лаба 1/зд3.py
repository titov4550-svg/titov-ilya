list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

middle_index = int(len(list_players) // 2)

first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

print(first_team)
print(second_team)