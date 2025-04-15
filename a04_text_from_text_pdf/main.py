import os
from PyPDF2 import PdfReader

# Пути к папкам (относительно расположения скрипта)
script_dir = os.path.dirname(os.path.abspath(__file__))  # Директория, где лежит скрипт
input_folder = os.path.join(script_dir, 'input')        # Папка input
output_folder = os.path.join(script_dir, 'output')      # Папка output
output_file = os.path.join(output_folder, 'output.txt') # Выходной файл

# Проверяем, существует ли папка output, если нет — создаём
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Открываем (или создаём) файл для записи текста
with open(output_file, 'w', encoding='utf-8') as outfile:
    # Проходим по всем файлам в папке input
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            # Полный путь к файлу
            file_path = os.path.join(input_folder, filename)
            
            # Открываем PDF-файл и извлекаем текст
            reader = PdfReader(file_path)
            text = ''
            for page in reader.pages:
                text += page.extract_text()
            
            # Записываем текст в выходной файл
            outfile.write(f"--- {filename} ---\n")
            outfile.write(text + "\n\n")

print(f"Текст из всех PDF-файлов сохранён в {output_file}")