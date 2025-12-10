def count_letters(text):  # TODO  Напишите функцию count_letters
    result = {}
    for letter in text.lower():
        if letter.isalpha():
            result[letter] = 0
    for char in result:
        for letter in text.lower():
            if letter.isalpha() and char == letter:
                result[char] += 1
    return result


def calculate_frequency(counted_letters):  # TODO Напишите функцию calculate_frequency
    total_count = 0
    for value in counted_letters.values():
        total_count += value
    for key, value in counted_letters.items():
        counted_letters.update({key: value / total_count})
    return counted_letters


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""


for name, value in calculate_frequency(count_letters(main_str)).items():  # TODO Распечатайте в столбик букву и её частоту в тексте
    print(f'{name}: {value:.2f}')