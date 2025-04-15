import os
import regex as re  # Используем расширенный regex

# Папки
input_dir = os.path.join(os.path.dirname(__file__), "input")
output_dir = os.path.join(os.path.dirname(__file__), "output")

# Имена выходных файлов
output_stat_file = os.path.join(output_dir, "word-list-stat.txt")
output_clean_file = os.path.join(output_dir, "word-list.txt")

# Регулярные выражения
LETTER_REGEX = re.compile(r"\p{L}", re.UNICODE)  # Буквы всех алфавитов
APOSTROPHE_REGEX = re.compile(r"[’'`]", re.UNICODE)  # Все апострофы (включая разные формы)
UPPERCASE_REGEX = re.compile(r"[A-ZА-Я]", re.UNICODE)  # Заглавные буквы

# Функция для проверки, содержит ли строка буквы
def contains_letters(text):
    return bool(LETTER_REGEX.search(text))

# Функция для проверки, состоит ли строка только из букв и апострофов
def contains_only_letters_and_apostrophes(text):
    return bool(re.fullmatch(r"[a-zA-Zа-яА-ЯёЁ\p{L}’'`]+", text))  # Только буквы и апострофы

# Функция для проверки, что строка содержит более 2 заглавных букв
def contains_two_or_more_uppercase(text):
    return len(UPPERCASE_REGEX.findall(text)) >= 2

# Функция для обработки одного файла
def process_file(input_file):
    # Читаем входной файл
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Преобразуем строки в двумерный массив
    word_list = []
    for line in lines:
        line = line.strip()  # Убираем лишние пробелы и символы перевода строки
        if "-" in line:
            word, number = line.rsplit(" - ", 1)  # Разделяем по последнему дефису
            if number.isdigit():  # Проверяем, что после дефиса число
                word_list.append([word, int(number)])

    # Фильтрация по новым правилам
    filtered_list = [
        entry for entry in word_list
        if contains_letters(entry[0])  # Содержит буквы
        and len(entry[0]) > 1  # Больше 2 символов
        and contains_only_letters_and_apostrophes(entry[0])  # Содержит только буквы и апострофы
        and not contains_two_or_more_uppercase(entry[0])  # Менее 2 заглавных букв
    ]

    # Записываем результаты в файлы
    # 1. Статистический файл с дефисом
    with open(output_stat_file, "w", encoding="utf-8") as stat_file:
        for word, number in filtered_list:
            stat_file.write(f"{word} - {number}\n")

    # 2. Чистый файл без дефиса и чисел
    with open(output_clean_file, "w", encoding="utf-8") as clean_file:
        for word, _ in filtered_list:
            clean_file.write(f"{word}\n")

    print(f"Processing of file '{os.path.basename(input_file)}' is complete.")
    print(f"Results saved in the 'output' folder.")

# Главная функция для поиска и обработки всех текстовых файлов
def main():
    # Проверяем наличие папки input
    if not os.path.exists(input_dir):
        print(f"The input folder '{input_dir}' does not exist.")
        return

    # Ищем текстовые файлы в папке input
    input_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith(".txt")]

    if not input_files:
        print("No text files found in the input folder.")
        return

    # Создаём выходную папку, если она не существует
    os.makedirs(output_dir, exist_ok=True)

    # Обрабатываем каждый файл
    for input_file in input_files:
        process_file(input_file)

if __name__ == "__main__":
    main()