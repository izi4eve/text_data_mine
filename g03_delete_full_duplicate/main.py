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
output_file = os.path.join(output_dir, 'no_duplicates.txt')

# Очищаем файл output, если он уже существует
if os.path.exists(output_file):
    os.remove(output_file)

# Множество для отслеживания строк, которые уже встречались
seen_lines = set()

# Список для результата
result_lines = []

# Проходим по строкам
for i in range(len(lines)):
    # Если строка уже была добавлена как дубль, пропускаем её
    if lines[i] in seen_lines:
        continue
    
    # Добавляем текущую строку в результат
    result_lines.append(lines[i])
    # Отмечаем, что строка встречалась
    seen_lines.add(lines[i])

# Записываем результат в файл
with open(output_file, 'w', encoding='utf-8') as out_file:
    for line in result_lines:
        out_file.write(line + '\n')

print("Обработка завершена. Результат записан в no_duplicates.txt в папке output.")