import pytest
import csv
import os
from typing import List, Dict

@pytest.fixture
def sample_csv_data() -> List[Dict]:
    return [
        {'product_id': '1', 'brand': 'Apple', 'rating': '4.5', 'price': '999'},
        {'product_id': '2', 'brand': 'Samsung', 'rating': '4.2', 'price': '799'},
        {'product_id': '3', 'brand': 'Apple', 'rating': '4.7', 'price': '1299'},
        {'product_id': '4', 'brand': 'Xiaomi', 'rating': '4.0', 'price': '299'},
    ]

@pytest.fixture
def sample_csv_file(tmp_path, sample_csv_data):
    csv_file = tmp_path / 'test_products.csv'

    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        if sample_csv_data:
            fieldnames = sample_csv_data[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(sample_csv_data)
        
    return str(csv_file)

@pytest.fixture
def empty_csv_file(tmp_path):
    csv_file = tmp_path / 'empty.csv'

    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['product_id', 'brand', 'rating', 'price'])
    
    return str(csv_file)

@pytest.fixture
def average_rating_report():
    from src.reports.average_rating import AverageRatingReport
    return AverageRatingReport()
