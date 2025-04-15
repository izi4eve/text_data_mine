import os
import spacy
import chardet

# Поддерживаемые языки и модели spaCy
LANG_MODELS = {
    'en': 'en_core_web_sm',
    'de': 'de_core_news_sm',
    'fr': 'fr_core_news_sm',
    'it': 'it_core_news_sm',
    'es': 'es_core_news_sm',
    'pt': 'pt_core_news_sm'
}

def detect_encoding(file_path):
    """
    Определяет кодировку файла.
    """
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    return result['encoding']

def lemmatize_text(language_code, input_text):
    """
    Лемматизирует текст на указанном языке.
    """
    if language_code not in LANG_MODELS:
        raise ValueError(f"Unsupported language code: {language_code}")
    
    # Загрузка модели spaCy
    try:
        nlp = spacy.load(LANG_MODELS[language_code])
    except OSError:
        print(f"Language model for {language_code} is not installed. Installing...")
        os.system(f"python -m spacy download {LANG_MODELS[language_code]}")
        nlp = spacy.load(LANG_MODELS[language_code])
    
    # Обработка текста
    doc = nlp(input_text)
    return " ".join([token.lemma_ for token in doc])

def process_files(language_code):
    """
    Проходит по всем файлам в папке input, лемматизирует их и сохраняет в папку output.
    """
    input_dir = os.path.join(os.path.dirname(__file__), 'input')
    output_dir = os.path.join(os.path.dirname(__file__), 'output')
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        if os.path.isfile(input_path):
            # Определяем кодировку файла
            encoding = detect_encoding(input_path)
            
            # Читаем файл с определённой кодировкой
            with open(input_path, 'r', encoding=encoding, errors='replace') as f:
                text = f.read()

            print(f"Processing file: {filename}")
            lemmatized_text = lemmatize_text(language_code, text)

            # Сохраняем результат в UTF-8
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(lemmatized_text)

if __name__ == "__main__":
    print("Supported languages: 'en', 'de', 'fr', 'it', 'es', 'pt'")
    lang_code = input("Enter the language code: ").strip().lower()

    if lang_code not in LANG_MODELS:
        print(f"Error: Unsupported language code '{lang_code}'. Exiting.")
    else:
        print(f"Starting lemmatization for language: {lang_code}")
        process_files(lang_code)
        print("Lemmatization completed. Check the 'output' folder.")