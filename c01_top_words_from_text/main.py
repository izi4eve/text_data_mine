import os
from collections import Counter

def process_text_files():
    # Указываем пути к папкам input и output
    input_dir = os.path.join(os.path.dirname(__file__), 'input')
    output_dir = os.path.join(os.path.dirname(__file__), 'output')
    
    # Создаем папку output, если её нет
    os.makedirs(output_dir, exist_ok=True)
    
    # Инициализируем общий список слов
    all_words = []

    # Проходим по всем файлам в папке input
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as file:
                # Читаем текст и добавляем слова в общий список
                text = file.read()
                words = text.split()
                all_words.extend(words)
    
    # Считаем частоту каждого слова с учётом регистра
    word_counts = Counter(all_words)
    
    # Сортируем по частоте (убывание), затем по алфавиту
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    
    # Путь к файлам вывода
    word_list_path = os.path.join(output_dir, 'word-list.txt')
    word_list_stat_path = os.path.join(output_dir, 'word-list-stat.txt')
    
    # Записываем слова в word-list-stat.txt
    with open(word_list_stat_path, 'w', encoding='utf-8') as word_list_stat_file:
        for word, count in sorted_word_counts:
            word_list_stat_file.write(f"{word} - {count}\n")
    
    # Записываем только слова (без частоты) в word-list.txt
    with open(word_list_path, 'w', encoding='utf-8') as word_list_file:
        for word, _ in sorted_word_counts:
            word_list_file.write(f"{word}\n")

if __name__ == "__main__":
    process_text_files()