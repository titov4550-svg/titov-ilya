import json

# Укажите имя файла
file_name = "input.json"  # ← если файл называется по-другому, поменяйте тут

# Открываем и читаем JSON
with open(file_name, 'r') as f:
    data = json.load(f)

# Считаем сумму score * weight
result = 0
for item in data:
    result += item['score'] * item['weight']

# Выводим результат
print(f"Сумма score * weight = {result}")