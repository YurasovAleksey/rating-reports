from typing import List, Dict
from collections import defaultdict
from tabulate import tabulate
from .base_report import BaseReport

class AverageRatingReport(BaseReport):
    
    def calculate(self, data: List[Dict]) -> List[Dict]:
        brand_ratings = defaultdict(list)
        
        for product in data:
            brand = product['brand']
            try:
                rating = float(product['rating'])
                brand_ratings[brand].append(rating)
            except (ValueError, KeyError):
                continue
        
        results = []
        for brand, ratings in brand_ratings.items():
            avg_rating = sum(ratings) / len(ratings)
            results.append({
                'brand': brand,
                'average_rating': round(avg_rating, 2)
            })
        
        results.sort(key=lambda x: x['average_rating'], reverse=True)
        
        return results
    
    def display(self, results: List[Dict]):
        
        if not results:
            print("📭 Нет данных для отображения")
            return
        
        table_data = []
        for i, item in enumerate(results, 1):
            table_data.append([
                i,
                item['brand'],
                item['average_rating']
            ])
        

        headers = ["№", "Бренд", "Средний рейтинг"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
        print(f"\n📈 Всего брендов: {len(results)}")
