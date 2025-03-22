import os
import zipfile
import shutil

def extract_and_sort(archive_path, output_dir):
    # Проверка и создание основной директории для результата
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Создаем временную директорию для распаковки архива
    temp_dir = os.path.join(output_dir, 'temp_extraction')
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    # Распаковка архива
    try:
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        print(f"Архив успешно распакован в {temp_dir}")
    except Exception as e:
        print("Ошибка при распаковке архива:", e)
        return

    # Обход всех файлов во временной директории
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            src_path = os.path.join(root, file)
            # Логика сортировки: пример на основе начала имени файла
            # Если имя файла начинается с "invoice" -> каталог "invoices"
            # Если имя файла начинается с "report"  -> каталог "reports"
            # Остальные файлы попадут в каталог "others"
            if file.lower().startswith("invoice"):
                category = "invoices"
            elif file.lower().startswith("report"):
                category = "reports"
            else:
                category = "others"
            
            dest_dir = os.path.join(output_dir, category)
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            
            dest_path = os.path.join(dest_dir, file)
            try:
                shutil.move(src_path, dest_path)
                print(f"Файл {file} перемещен в {category}")
            except Exception as e:
                print(f"Ошибка при перемещении файла {file}: {e}")
    
    # Удаление временной директории после обработки
    try:
        shutil.rmtree(temp_dir)
        print("Временная директория удалена.")
    except Exception as e:
        print("Ошибка при удалении временной директории:", e)

    print("Обработка и сортировка данных завершены.")

if __name__ == '__main__':
    archive_path = input("Введите путь к архиву: ")
    output_dir = input("Введите путь для сохранения отсортированных файлов: ")
    extract_and_sort(archive_path, output_dir)

