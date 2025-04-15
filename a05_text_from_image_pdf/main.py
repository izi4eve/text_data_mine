import os
from pdf2image import convert_from_path
import pytesseract
from PIL import Image

# Словарь языков
LANGUAGES = {
    1: 'eng',  # Английский
    2: 'deu',  # Немецкий
    3: 'fra',  # Французский
    4: 'ita',  # Итальянский
    5: 'spa',  # Испанский
    6: 'por',  # Португальский
}

# Функция для выбора языка
def select_language():
    print("Выберите язык для распознавания текста:")
    for num, lang in LANGUAGES.items():
        print(f"{num}: {lang}")
    while True:
        try:
            choice = int(input("Введите номер языка: "))
            if choice in LANGUAGES:
                return LANGUAGES[choice]
            else:
                print("Неверный номер. Попробуйте снова.")
        except ValueError:
            print("Введите число.")

# Пути к папкам (относительно расположения скрипта)
script_dir = os.path.dirname(os.path.abspath(__file__))  # Директория, где лежит скрипт
input_folder = os.path.join(script_dir, 'input')        # Папка input
output_folder = os.path.join(script_dir, 'output')      # Папка output
output_file = os.path.join(output_folder, 'output.txt') # Выходной файл

# Проверяем, существует ли папка output, если нет — создаём
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Выбираем язык
selected_lang = select_language()

# Открываем (или создаём) файл для записи текста
with open(output_file, 'w', encoding='utf-8') as outfile:
    # Проходим по всем файлам в папке input
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            # Полный путь к файлу
            file_path = os.path.join(input_folder, filename)
            
            # Преобразуем PDF в список изображений (по одной странице)
            images = convert_from_path(file_path)
            
            # Обрабатываем каждое изображение
            text = ''
            for i, image in enumerate(images):
                # Применяем OCR к изображению
                page_text = pytesseract.image_to_string(image, lang=selected_lang)
                text += f"--- Страница {i + 1} ---\n{page_text}\n\n"
            
            # Записываем текст в выходной файл
            outfile.write(f"--- {filename} ---\n")
            outfile.write(text + "\n\n")

print(f"Текст из всех PDF-файлов сохранён в {output_file}")