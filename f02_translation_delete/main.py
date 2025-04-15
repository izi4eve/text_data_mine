import os

def process_file(input_file_path, output_file_path):
    """
    Обрабатывает файл: удаляет часть строки после знака "=" и сохраняет результат в новый файл.
    :param input_file_path: Путь к входному файлу.
    :param output_file_path: Путь для сохранения обработанного файла.
    """
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        lines = input_file.readlines()

    # Обрабатываем каждую строку
    processed_lines = []
    for line in lines:
        # Убираем пробелы в начале и конце строки
        line = line.strip()
        if '=' in line:
            # Оставляем только часть до " = " (включая сам знак равно и пробел)
            processed_line = ' '.join(line.split('=')[0].split()) + ' = '
        else:
            # Если нет знака равно, оставляем строку без изменений
            processed_line = line
        processed_lines.append(processed_line)

    # Записываем обработанные строки в выходной файл
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write('\n'.join(processed_lines))

def main():
    # Путь к папке, где находится скрипт
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_folder = os.path.join(current_dir, 'input')
    output_folder = os.path.join(current_dir, 'output')

    # Убедимся, что папка для вывода существует
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Поиск текстовых файлов в папке input
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):  # Проверяем, что это текстовый файл
            input_file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_folder, filename)

            # Обрабатываем файл
            process_file(input_file_path, output_file_path)
            print(f"Processed file: {filename} -> output/{filename}")

if __name__ == '__main__':
    main()