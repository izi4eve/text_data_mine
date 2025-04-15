from googletrans import Translator
import os

# Инициализация переводчика
translator = Translator()

# Определение путей к файлам
script_dir = os.path.dirname(os.path.abspath(__file__))  # Получаем директорию текущего скрипта
input_file_path = os.path.join(script_dir, 'input/without-translation.txt')
output_file_path = os.path.join(script_dir, 'output/translated_german_words_dict.txt')

# Создаем директорию output, если она не существует
os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

# Чтение списка слов из файла
with open(input_file_path, 'r', encoding='utf-8') as file:
    words = [line.strip() for line in file]

# Перевод слов на русский
translated_dict = {}
for word in words:
    try:
        translated = translator.translate(word, src='de', dest='ru')
        translated_dict[word] = translated.text
    except Exception as e:
        print(f"Ошибка при переводе слова '{word}': {e}")

# Запись переведенного словаря в новый файл
with open(output_file_path, 'w', encoding='utf-8') as file:
    for german_word, russian_translation in translated_dict.items():
        file.write(f"{german_word}: {russian_translation}\n")