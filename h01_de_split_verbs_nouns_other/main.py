import os

def process_file():
    # Определяем пути к папкам
    input_dir = os.path.join(os.path.dirname(__file__), 'input')
    output_dir = os.path.join(os.path.dirname(__file__), 'output')

    # Проверяем наличие папки input и output
    if not os.path.exists(input_dir):
        print("Папка 'input' не найдена.")
        return
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Получаем первый текстовый файл из папки input
    input_files = [f for f in os.listdir(input_dir) if f.endswith('.txt')]
    if not input_files:
        print("There is no files in 'input' folder.")
        return
    
    input_file_path = os.path.join(input_dir, input_files[0])

    # Создаём пути для файлов результата
    nouns_file = os.path.join(output_dir, 'nouns.txt')
    verbs_file = os.path.join(output_dir, 'verbs.txt')
    other_file = os.path.join(output_dir, 'other.txt')

    # Инициализируем списки для сортировки строк
    nouns = []
    verbs = []
    others = []

    # Читаем входной файл и сортируем строки
    with open(input_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line.startswith(('der ', 'die ', 'das ')):
                nouns.append(line)
            elif '—' in line:
                verbs.append(line)
            else:
                others.append(line)

    # Записываем результаты в соответствующие файлы
    with open(nouns_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(nouns))
    with open(verbs_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(verbs))
    with open(other_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(others))
    
    print(f"Files created in folder 'output':\n - nouns.txt\n - verbs.txt\n - other.txt")

if __name__ == '__main__':
    process_file()