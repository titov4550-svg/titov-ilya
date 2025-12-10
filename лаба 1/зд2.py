volume = 1.44  # В Мб
number_pages = 100
number_strings = 50
number_symbols = 25
symbol_volume = 4  # В б

count_books = int((volume * 1024 ** 2) // (number_pages * number_strings * number_symbols * symbol_volume))
print("Количество книг, помещающихся на дискету:", count_books)