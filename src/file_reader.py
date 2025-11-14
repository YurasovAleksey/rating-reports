import csv
from typing import List, Dict


def read_csv_files(file_paths: List[str]) -> List[Dict]:
    data = []

    for file_path in file_paths:
        try:
            print(f"📖 Читаем файл: {file_path}")
            
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    data.append(row)
                    
                print(f"✅ Прочитано {len(list(reader))} строк из {file_path}")
                
        except FileNotFoundError:
            print(f"❌ Файл не найден: {file_path}")
            raise
        except Exception as e:
            print(f"❌ Ошибка при чтении {file_path}: {e}")
            raise
    
    print(f"📊 Всего прочитано {len(data)} записей")
    return data
