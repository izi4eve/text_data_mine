import os
from PIL import Image
import pytesseract

# Устанавливаем переменную окружения вручную перед использованием pytesseract
os.environ['TESSDATA_PREFIX'] = '/opt/homebrew/share/tessdata/'

# Выводим текущую переменную окружения для диагностики
print("TESSDATA_PREFIX:", os.environ.get('TESSDATA_PREFIX'))

# Пути к папкам
input_folder = os.path.join(os.path.dirname(__file__), "input")
output_folder = os.path.join(os.path.dirname(__file__), "output")
output_file = os.path.join(output_folder, "combined_text.txt")

# Поддерживаемые языки (трёхбуквенные коды)
supported_languages = {
    "eng": "English",
    "deu": "German",
    "fra": "French",
    "ita": "Italian",
    "spa": "Spanish",
    "por": "Portuguese"
}

def get_language():
    print("Supported languages:")
    for code, name in supported_languages.items():
        print(f"'{code}' - {name}")
    lang = input("Enter the language code: ").strip().lower()
    if lang not in supported_languages:
        print("Invalid language code. Defaulting to 'eng' (English).")
        lang = "eng"
    return lang

def extract_text_from_images(input_dir, output_path, lang):
    if not os.path.exists(output_path):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    combined_text = ""

    for file_name in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file_name)
        
        # Проверяем, что файл является изображением
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            try:
                print(f"Processing file: {file_name} with language: {lang}")
                image = Image.open(file_path)
                # Указываем только код языка (например "deu", без полного пути)
                text = pytesseract.image_to_string(image, lang=lang)
                combined_text += text + "\n\n"
            except Exception as e:
                print(f"Error processing file {file_name}: {e}")

    # Сохраняем объединённый текст в файл
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(combined_text)
    print(f"Combined text saved to file: {output_path}")

if __name__ == "__main__":
    selected_language = get_language()
    extract_text_from_images(input_folder, output_file, selected_language)