import os
import shutil

def clear_input_output_folders(base_dir):
    """
    Проходит по всем папкам в указанной директории и удаляет содержимое папок input и output.
    :param base_dir: Директория, в которой находится скрипт.
    """
    # Получаем список всех папок в директории base_dir
    for root, dirs, _ in os.walk(base_dir):
        for folder in ['input', 'output', 'foreign', 'translate']:
            folder_path = os.path.join(root, folder)
            if os.path.exists(folder_path):
                print(f"Clearing folder: {folder_path}")
                # Удаляем все содержимое папки
                for item in os.listdir(folder_path):
                    item_path = os.path.join(folder_path, item)
                    if os.path.isfile(item_path) or os.path.islink(item_path):
                        os.unlink(item_path)  # Удаляем файл или ссылку
                    elif os.path.isdir(item_path):
                        shutil.rmtree(item_path)  # Удаляем папку и её содержимое
                print(f"Folder {folder_path} cleared.")

def main():
    # Определяем текущую директорию скрипта
    script_dir = os.path.dirname(os.path.realpath(__file__))
    
    # Очищаем input и output папки
    clear_input_output_folders(script_dir)

if __name__ == '__main__':
    main()