import os

def read_text_files_from_folder(folder_path):
    """
    Читает все текстовые файлы в указанной папке и возвращает список строк.
    :param folder_path: Путь к папке с текстовыми файлами.
    :return: Список строк из всех файлов в папке.
    """
    file_lines = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):  # Проверка на текстовые файлы
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                file_lines.extend(lines)
    # Убираем пустые строки
    return [line.strip() for line in file_lines if line.strip()]

def create_translation_file(foreign_lines, translate_lines, output_folder):
    """
    Создает файл с сопоставлениями иностранных фраз и переводов.
    :param foreign_lines: Список иностранных фраз.
    :param translate_lines: Список переводов.
    :param output_folder: Папка для сохранения файла.
    """
    # Название выходного файла
    output_filename = os.path.join(output_folder, "translations.txt")
    
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        # Проходим по обоим спискам одновременно
        for foreign, translate in zip(foreign_lines, translate_lines):
            output_file.write(f"{foreign} = {translate}\n")
    
    print(f"Translations saved to {output_filename}")

def main():
    # Папки, содержащие входные файлы
    current_dir = os.path.dirname(os.path.realpath(__file__))  # Папка, где находится скрипт
    input_foreign_folder = os.path.join(current_dir, 'input_foreign')
    input_translate_folder = os.path.join(current_dir, 'input_translate')
    output_folder = os.path.join(current_dir, 'output')

    # Убедимся, что папка для вывода существует
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Читаем файлы из обеих папок
    foreign_lines = read_text_files_from_folder(input_foreign_folder)
    translate_lines = read_text_files_from_folder(input_translate_folder)
    
    # Проверка на совпадение длины списков
    if len(foreign_lines) != len(translate_lines):
        print("The number of foreign lines does not match the number of translation lines.")
        return
    
    # Создаем файл с переводами
    create_translation_file(foreign_lines, translate_lines, output_folder)

if __name__ == '__main__':
    main()