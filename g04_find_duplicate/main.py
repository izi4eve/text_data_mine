import os

# Получаем путь к текущей подпапке, где лежит скрипт
current_dir = os.path.dirname(os.path.abspath(__file__))

# Задаём пути к папкам input и output
input_dir = os.path.join(current_dir, 'input')
output_dir = os.path.join(current_dir, 'output')

# Убеждаемся, что папка output существует
os.makedirs(output_dir, exist_ok=True)

# Находим единственный текстовый файл в папке input
input_files = [f for f in os.listdir(input_dir) if f.endswith('.txt')]
if not input_files:
    print("В папке input нет текстовых файлов!")
    exit()
elif len(input_files) > 1:
    print("В папке input должен быть только один текстовый файл!")
    exit()

input_file_path = os.path.join(input_dir, input_files[0])

# Читаем все строки из файла
with open(input_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Убираем символы перевода строки
lines = [line.strip() for line in lines]

# Путь для выходного файла
output_file = os.path.join(output_dir, 'matches.txt')

# Очищаем файл output, если он уже существует
if os.path.exists(output_file):
    os.remove(output_file)

# Множество для отслеживания обработанных подстрок
processed_substrings = set()

# Проходим по строкам
for i in range(len(lines)):
    # Проверяем, есть ли хотя бы два пробела в строке
    if lines[i].count(' ') < 2:
        continue
    
    # Берём подстроку от начала до второго пробела
    substring = ' '.join(lines[i].split(' ')[:2])
    
    # Если подстрока уже обработана, пропускаем
    if substring in processed_substrings:
        continue
    
    # Ищем первое совпадение в оставшихся строках
    for j in range(i + 1, len(lines)):
        if lines[j].count(' ') >= 2:
            current_substring = ' '.join(lines[j].split(' ')[:2])
            if current_substring == substring:
                # Добавляем только первую строку с совпадением
                with open(output_file, 'a', encoding='utf-8') as out_file:
                    out_file.write(lines[j] + '\n')
                # Добавляем подстроку в обработанные
                processed_substrings.add(substring)
                break  # Выходим после первого совпадения

print("Обработка завершена. Результат записан в matches.txt в папке output.")