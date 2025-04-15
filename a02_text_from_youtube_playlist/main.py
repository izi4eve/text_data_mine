import os
import re
from pytube import YouTube, Playlist  # Для работы с видео и плейлистами
from youtube_transcript_api import YouTubeTranscriptApi  # Для получения субтитров с видео

def process_subtitles(subtitles):
    """Обрабатывает субтитры, форматируя их в виде полных предложений."""
    lines = subtitles.split('\n')
    result = []
    current_sentence = ""
    sentence_endings = {'.', '!', '?', ':', ';'}

    for line in lines:
        line = line.strip()
        if not line:
            continue
        current_sentence += ' ' + line
        if current_sentence[-1] in sentence_endings:
            result.append(current_sentence.strip())
            current_sentence = ""

    if current_sentence:
        result.append(current_sentence.strip())

    return '\n'.join(result)

def get_subtitles(video_url, language_code, output_folder):
    """
    Загружает субтитры с видео YouTube и сохраняет их в файл.
    :param video_url: URL видео на YouTube
    :param language_code: Код языка для субтитров (например, 'en', 'de', 'fr')
    :param output_folder: Папка для сохранения результатов
    """
    video_id = video_url.split('v=')[-1]

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language_code])
        subtitles = [entry['text'] for entry in transcript]
        subtitles_text = "\n".join(subtitles)
        processed_subtitles = process_subtitles(subtitles_text)
        output_filename = f"{output_folder}/{language_code}_{video_id}.txt"

        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(processed_subtitles)

        print(f"Subtitles for video {video_id} saved as {output_filename}")
    except Exception as e:
        print(f"Error retrieving subtitles for video {video_id}: {e}")

def main():
    # Запрашиваем ссылку на плейлист
    playlist_url = input("Enter YouTube playlist URL: ").strip()

    # Проверяем, что это корректная ссылка
    if not playlist_url.startswith("https://www.youtube.com/playlist?"):
        print("Invalid playlist URL. Please provide a valid YouTube playlist link.")
        return

    # Запрашиваем язык субтитров
    language_code = input("Enter subtitle language code (en, de, fr, it, es, pt): ").strip().lower()
    valid_languages = ['en', 'de', 'fr', 'it', 'es', 'pt']
    if language_code not in valid_languages:
        print("Invalid language code. Please enter a valid code (en, de, fr, it, es, pt).")
        return

    # Создаем папку output
    output_folder = os.path.dirname(os.path.realpath(__file__))
    output_folder = os.path.join(output_folder, 'output')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Получаем все видео из плейлиста
    try:
        playlist = Playlist(playlist_url)
        print(f"Found {len(playlist.video_urls)} videos in the playlist.")

        for video_url in playlist.video_urls:
            print(f"Processing video: {video_url}")
            get_subtitles(video_url, language_code, output_folder)

    except Exception as e:
        print(f"Error processing playlist: {e}")

if __name__ == '__main__':
    main()