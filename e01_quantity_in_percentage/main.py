import os

def read_file(file_path):
    """Читает файл и возвращает массив данных в формате [строка, число]."""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = []
        for line in file:
            parts = line.strip().split(" - ")
            if len(parts) == 2 and parts[1].isdigit():
                data.append([parts[0], int(parts[1])])
        return data

def get_user_percentage():
    """Запрашивает процент у пользователя и валидирует его."""
    while True:
        user_input = input("Please enter the desired word frequency percentage (from 1 to 100): ").strip()
        if user_input.isdigit():
            percentage = int(user_input)
            if 1 <= percentage <= 100:
                return percentage
        print("You entered an invalid value. Please try again with a number between 1 and 100.")

def calculate_covering_records(data, target_percentage):
    """Находит минимальное количество записей, покрывающее заданный процент от общей суммы."""
    total_sum = sum(item[1] for item in data)
    target_sum = (total_sum * target_percentage) / 100
    cumulative_sum = 0

    for index, item in enumerate(data, start=1):
        cumulative_sum += item[1]
        if cumulative_sum >= target_sum:
            return index, target_percentage

def main():
    # Определение пути к папке input
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(script_dir, 'input')

    # Поиск текстового файла в папке input
    text_files = [f for f in os.listdir(input_dir) if f.endswith('.txt')]
    if not text_files:
        print("No text files found in the 'input' directory.")
        return

    # Чтение данных из файла
    file_path = os.path.join(input_dir, text_files[0])
    data = read_file(file_path)
    if not data:
        print("The input file is empty or has an invalid format.")
        return

    # Запрос процента у пользователя
    target_percentage = get_user_percentage()

    # Расчет количества записей
    result = calculate_covering_records(data, target_percentage)
    if result:
        index, percentage = result
        print(f"{index} records cover your {percentage}% target.")
    else:
        print("An error occurred during the calculation.")

if __name__ == "__main__":
    main()