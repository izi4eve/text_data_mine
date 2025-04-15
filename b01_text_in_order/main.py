import os
import chardet

def detect_encoding(file_path):
    """Определяет кодировку файла."""
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    return result['encoding']

def process_file(input_folder, output_folder):
    # Получаем абсолютный путь к текущей директории
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Папки input и output относительно этой директории
    input_folder = os.path.join(base_dir, input_folder)
    output_folder = os.path.join(base_dir, output_folder)
    
    # Получаем все файлы в папке input
    input_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]
    
    # Обрабатываем каждый файл
    for file_name in input_files:
        input_file_path = os.path.join(input_folder, file_name)
        output_file_path = os.path.join(output_folder, file_name)
        
        # Определяем кодировку входного файла
        encoding = detect_encoding(input_file_path)
        
        # Читаем файл с определённой кодировкой
        with open(input_file_path, 'r', encoding=encoding, errors='replace') as input_file:
            lines = input_file.readlines()
        
        processed_lines = []
        skip_next = False  # Флаг для пропуска строки
        
        for i, line in enumerate(lines):
            line = line.strip()  # Убираем начальные и конечные пробелы

            # Пропускаем пустые строки
            if not line:
                processed_lines.append(line)  # Пустая строка добавляется в результат
                continue

            # Удаляем строки длиной от 1 до 5 символов, но оставляем пустые строки
            if line and len(line) <= 5:
                continue

            # Обработка строк, которые не заканчиваются на точку, восклицательный знак или вопросительный знак
            if not line[-1] in ['.', '!', '?']:
                if i + 1 < len(lines) and lines[i + 1].strip():  # Если следующая строка не пустая
                    line += ' ' + lines[i + 1].strip()  # Соединяем строки через пробел
                    skip_next = True  # Пропускаем следующую строку

            # Удаление дефиса и соединение строк без пробела
            if line.endswith('-'):
                # Проверяем, что перед дефисом есть буква
                if line[-2].isalpha():
                    # Присоединяем следующую строку без пробела
                    line = line[:-1] + lines[i + 1].strip() if i + 1 < len(lines) else line[:-1]
                    skip_next = True  # Пропускаем следующую строку

            # Удаление строк, которые не содержат букв
            if not any(c.isalpha() for c in line):
                continue

            # Добавляем пробелы вокруг дроби (если нет пробела до и после "/")
            line = line.replace('/', ' / ')
            line = line.replace('-', ' - ')

            # Добавляем обработанную строку в результат
            if not skip_next:
                processed_lines.append(line)
            skip_next = False
        
        # Сохраняем результат в новый файл в output с кодировкой UTF-8
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write('\n'.join(processed_lines))

# Путь к папкам input и output (относительно папки, где находится скрипт)
input_folder = 'input'
output_folder = 'output'

# Запуск обработки
process_file(input_folder, output_folder)