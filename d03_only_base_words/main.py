import spacy
import os

# Загружаем модель для немецкого языка
nlp = spacy.load("de_core_news_sm")

def is_valid_word(token):
    # Проверяем, является ли токен основным словом (не числительным, местоимением, предлогом и т.д.)
    return token.pos_ in ("NOUN", "VERB", "ADJ", "ADV") and not token.is_stop

def clean_words(input_dir, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for filename in os.listdir(input_dir):
            if filename.endswith('.txt'):
                input_file_path = os.path.join(input_dir, filename)
                with open(input_file_path, 'r', encoding='utf-8') as infile:
                    for line in infile:
                        word = line.strip()
                        if word:  # Проверяем, что строка не пустая
                            doc = nlp(word)
                            for token in doc:
                                if is_valid_word(token) and token.text.lower() == token.lemma_.lower():
                                    outfile.write(token.text + '\n')

# Определяем абсолютные пути к директориям
base_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.join(base_dir, 'input')
output_file = os.path.join(base_dir, 'output', 'output.txt')

# Используем функцию для очистки файлов
clean_words(input_dir, output_file)