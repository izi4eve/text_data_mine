import os
import re
from pytube import YouTube  # Для работы с отдельными видео YouTube
from youtube_transcript_api import YouTubeTranscriptApi  # Для получения субтитров с видео

def process_subtitles(subtitles):
    # Разделяем текст на строки
    lines = subtitles.split('\n')
    
    # Список для хранения обработанных предложений
    result = []
    
    # Вспомогательная переменная для накопления предложений
    current_sentence = ""
    
    # Знаки, на которые должна заканчиваться строка
    sentence_endings = {'.', '!', '?', ':', ';'}
    
    for line in lines:
        # Убираем лишние пробелы по краям строки
        line = line.strip()
        
        # Если строка пустая, пропускаем её
        if not line:
            continue
        
        # Добавляем строку к текущему предложению
        current_sentence += ' ' + line
        
        # Проверяем, заканчивается ли текущее предложение на нужный знак
        if current_sentence[-1] in sentence_endings:
            # Если заканчивается на знак, добавляем предложение в результат
            result.append(current_sentence.strip())
            # Сбрасываем накопленное предложение
            current_sentence = ""
    
    # Если в конце осталась незавершенная строка (например, без знака окончания)
    if current_sentence:
        result.append(current_sentence.strip())
    
    # Объединяем все предложения в финальный текст
    return '\n'.join(result)


def get_subtitles(video_url, language_code):
    """
    Эта функция принимает URL видео и код языка, получает субтитры и сохраняет их в файл.
    
    :param video_url: URL видео на YouTube
    :param language_code: Код языка для субтитров (например, 'en', 'de', 'fr')
    """
    # Получаем ID видео из URL
    video_id = video_url.split('v=')[-1]
    
    # Папка для хранения выходных файлов (создается в директории скрипта)
    output_folder = os.path.dirname(os.path.realpath(__file__))  # Папка, где находится скрипт
    output_folder = os.path.join(output_folder, 'output')
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Получаем субтитры для видео на указанном языке
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language_code])
        
        # Собираем только текст из субтитров
        subtitles = [entry['text'] for entry in transcript]
        
        # Объединяем список строк в одну строку
        subtitles_text = "\n".join(subtitles)

        # Обрабатываем субтитры
        processed_subtitles = process_subtitles(subtitles_text)

        # Название файла будет как 'languageCode_videoID.txt'
        output_filename = f"{output_folder}/{language_code}_{video_id}.txt"
        
        # Сохраняем субтитры в файл
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(processed_subtitles)
        
        print(f"Subtitles for {video_url} saved as {output_filename}")
    except Exception as e:
        print(f"Error retrieving subtitles for {video_url}: {e}")

def main():
    # Спрашиваем ссылку на видео
    video_url = input("Enter YouTube video URL: ")

    # Спрашиваем язык субтитров
    language_code = input("Enter subtitle language code (en, de, fr, it, es, pt): ").strip().lower()

    # Проверяем, что код языка является валидным
    valid_languages = ['en', 'de', 'fr', 'it', 'es', 'pt']
    if language_code not in valid_languages:
        print("Invalid language code. Please enter a valid code (en, de, fr, it, es, pt).")
        return

    # Получаем субтитры для указанного видео и языка
    get_subtitles(video_url, language_code)

if __name__ == '__main__':
    main()