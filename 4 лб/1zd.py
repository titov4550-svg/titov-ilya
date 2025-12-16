"""
Конвертер CSV в JSON
Преобразует данные из CSV формата в JSON
"""

import csv
import json


def read_csv_data(file_path, delimiter=','):
    """
    Читает данные из CSV файла

    Args:
        file_path (str): Путь к CSV файлу
        delimiter (str): Разделитель полей (',' или ';')

    Returns:
        list: Список словарей с данными
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=delimiter)
        return list(reader)


def save_json_data(data, file_path, indent=2):
    """
    Сохраняет данные в JSON файл

    Args:
        data (list): Данные для сохранения
        file_path (str): Путь к JSON файлу
        indent (int): Отступ для форматирования
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=indent)


def detect_delimiter(file_path):
    """
    Определяет разделитель в CSV файле

    Args:
        file_path (str): Путь к CSV файлу

    Returns:
        str: Разделитель (',' или ';')
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        first_line = file.readline()

    return ';' if ';' in first_line else ','


def convert_csv_to_json(csv_file, json_file=None, delimiter=None):
    """
    Основная функция конвертации

    Args:
        csv_file (str): Путь к CSV файлу
        json_file (str): Путь к JSON файлу (опционально)
        delimiter (str): Разделитель CSV (опционально)

    Returns:
        bool: True при успешной конвертации
    """
    try:
        # Определяем выходной файл
        if not json_file:
            if csv_file.endswith('.csv'):
                json_file = csv_file[:-4] + '.json'
            else:
                json_file = csv_file + '.json'

        # Определяем разделитель
        if not delimiter:
            delimiter = detect_delimiter(csv_file)

        # Читаем CSV
        data = read_csv_data(csv_file, delimiter)

        # Сохраняем JSON
        save_json_data(data, json_file)

        # Выводим результат
        print(f"✓ Конвертация завершена")
        print(f"  CSV: {csv_file}")
        print(f"  JSON: {json_file}")
        print(f"  Записей: {len(data)}")

        return True

    except FileNotFoundError:
        print(f"✗ Ошибка: файл '{csv_file}' не найден")
        return False
    except Exception as e:
        print(f"✗ Ошибка: {e}")
        return False


def main():
    """
    Точка входа в программу
    """
    print("=== Конвертер CSV в JSON ===")

    # Запрашиваем имя CSV файла
    csv_file = input("Введите имя CSV файла: ").strip()

    if not csv_file:
        print("✗ Не указано имя файла")
        return

    # Запускаем конвертацию
    convert_csv_to_json(csv_file)


# Запуск программы
if __name__ == "__main__":
    main()
