import argparse
from file_reader import read_csv_files
from reports.average_rating import AverageRatingReport


def main():
    print('Rating Reports Generator')

    parser = argparse.ArgumentParser(description='Генератор отчетов по товарам')

    parser.add_argument(
        '--files',
        nargs='+',
        required=True,
        help='Пути к csv-файлам с данными'
    )

    parser.add_argument(
        '--report',
        required=True,
        choices=['average-rating'],
        help='Тип отчета'
    )

    args = parser.parse_args()

    if args.report == 'average-rating':
        report = AverageRatingReport()
    else:
        print(f"❌ Неизвестный тип отчета: {args.report}")
        return
    
    try:
        print(f"📁 Файлы: {', '.join(args.files)}")
        data = read_csv_files(args.files)
        
        print(f"📊 Генерация отчета: {args.report}")
        print("-" * 40)
        
        report.generate(data)
        
    except Exception as e:
        print(f"💥 Ошибка: {e}")
        return

if __name__ == '__main__':
    main()
