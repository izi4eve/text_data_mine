import os

def process_files(input_folder, minus_folder, output_folder):
    """
    Обрабатывает файлы: удаляет строки из первого файла на основании второго и сохраняет результат.
    :param input_folder: Путь к папке с исходным текстовым файлом.
    :param minus_folder: Путь к папке с файлом исключений.
    :param output_folder: Путь к папке для сохранения результата.
    """
    # Получаем файлы из папок
    input_files = [f for f in os.listdir(input_folder) if f.endswith('.txt')]
    minus_files = [f for f in os.listdir(minus_folder) if f.endswith('.txt')]

    if not input_files or not minus_files:
        print("No input or minus files found.")
        return

    # Используем первый файл из каждой папки
    input_file_path = os.path.join(input_folder, input_files[0])
    minus_file_path = os.path.join(minus_folder, minus_files[0])

    # Читаем данные из input
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        input_lines = input_file.readlines()

    # Читаем данные из minus
    with open(minus_file_path, 'r', encoding='utf-8') as minus_file:
        minus_lines = set(line.strip() for line in minus_file if line.strip())

    # Преобразуем input_lines в массив
    array = []
    for line in input_lines:
        line = line.strip()
        if " - " in line:
            word, number = map(str.strip, line.split(" - ", 1))
            array.append([word, number])

    # Фильтруем массив на основе данных из minus
    filtered_array = [item for item in array if item[0] not in minus_lines]

    # Готовим данные для записи
    word_list_stat = "\n".join(f"{item[0]} - {item[1]}" for item in filtered_array)
    word_list = "\n".join(item[0] for item in filtered_array)

    # Убедимся, что папка output существует
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Сохраняем результаты
    with open(os.path.join(output_folder, "word-list-stat.txt"), 'w', encoding='utf-8') as stat_file:
        stat_file.write(word_list_stat)

    with open(os.path.join(output_folder, "word-list.txt"), 'w', encoding='utf-8') as list_file:
        list_file.write(word_list)

    print(f"Processing completed. Results saved to '{output_folder}'.")

def main():
    # Определяем пути
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_folder = os.path.join(current_dir, 'input')
    minus_folder = os.path.join(current_dir, 'minus')
    output_folder = os.path.join(current_dir, 'output')

    # Запускаем обработку
    process_files(input_folder, minus_folder, output_folder)

if __name__ == '__main__':
    main()