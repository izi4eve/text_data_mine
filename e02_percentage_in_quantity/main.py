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

def get_user_index(max_index):
    """Запрашивает индекс у пользователя и валидирует его."""
    while True:
        user_input = input(f"Please enter a number between 1 and {max_index} to calculate frequency percentage: ").strip()
        if user_input.isdigit():
            index = int(user_input)
            if 1 <= index <= max_index:
                return index
        print(f"Invalid input. Please enter a number between 1 and {max_index}.")

def calculate_percentage(data, index):
    """Вычисляет процент частоты для записей до указанного индекса."""
    total_sum = sum(item[1] for item in data)
    partial_sum = sum(data[i][1] for i in range(index))
    percentage = (partial_sum / total_sum) * 100
    return round(percentage, 2)

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

    # Запрос индекса у пользователя
    max_index = len(data)
    user_index = get_user_index(max_index)

    # Расчет процента
    percentage = calculate_percentage(data, user_index)
    print(f"The words up to index {user_index} cover {percentage}% of the total frequency.")

if __name__ == "__main__":
    main()