import os

# Получаем путь к текущей подпапке, где лежит скрипт
current_dir = os.path.dirname(os.path.abspath(__file__))

# Задаём пути к папкам dics, input и output
dics_dir = os.path.join(current_dir, 'dics')
input_dir = os.path.join(current_dir, 'input')
output_dir = os.path.join(current_dir, 'output')

# Убеждаемся, что папка output существует
os.makedirs(output_dir, exist_ok=True)

# Находим текстовый файл в папке dics
dics_files = [f for f in os.listdir(dics_dir) if f.endswith('.txt')]
if not dics_files:
    print("В папке dics нет текстовых файлов!")
    exit()
elif len(dics_files) > 1:
    print("В папке dics должен быть только один текстовый файл!")
    exit()

dics_file_path = os.path.join(dics_dir, dics_files[0])

# Находим текстовый файл в папке input
input_files = [f for f in os.listdir(input_dir) if f.endswith('.txt')]
if not input_files:
    print("В папке input нет текстовых файлов!")
    exit()
elif len(input_files) > 1:
    print("В папке input должен быть только один текстовый файл!")
    exit()

input_file_path = os.path.join(input_dir, input_files[0])

# Читаем файл из dics и собираем подстроки для сравнения
substrings_to_compare = set()
with open(dics_file_path, 'r', encoding='utf-8') as dics_file:
    dics_lines = [line.strip() for line in dics_file.readlines()]

for line in dics_lines:
    # Разделяем строку по пробелам
    parts = line.split(' ')
    if len(parts) >= 1:  # Проверяем, есть ли хотя бы одна часть
        first_part = parts[0]  # Подстрока до первого пробела (без пробела)
        # Если первая часть — der, die или das
        if first_part in {"der", "die", "das"} and len(parts) >= 2:
            # Берем подстроку между первым и вторым пробелами (без пробелов)
            second_part = parts[1]
            substrings_to_compare.add(second_part)
        else:
            # Иначе берем первую часть
            substrings_to_compare.add(first_part)

# Читаем файл из input
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    input_lines = [line.strip() for line in input_file.readlines()]

# Фильтруем строки из input: оставляем только те, которых нет в substrings_to_compare
result_lines = [line for line in input_lines if line not in substrings_to_compare]

# Путь для выходного файла
output_file = os.path.join(output_dir, 'filtered_output.txt')

# Очищаем файл output, если он уже существует
if os.path.exists(output_file):
    os.remove(output_file)

# Записываем результат в файл
with open(output_file, 'w', encoding='utf-8') as out_file:
    for line in result_lines:
        out_file.write(line + '\n')

print("Обработка завершена. Результат записан в filtered_output.txt в папке output.")