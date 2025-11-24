import pytest
import csv
import os
from src.file_reader import read_csv_files

class TestFileReader:
    def test_read_single_file(self, sample_csv_file, sample_csv_data):
        result = read_csv_files([sample_csv_file])
        
        assert len(result) == len(sample_csv_data)
        assert result == sample_csv_data
    
    def test_read_multiple_files(self, sample_csv_file, tmp_path):
        second_file = tmp_path / "products2.csv"
        with open(second_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['product_id', 'brand', 'rating', 'price'])
            writer.writeheader()
            writer.writerow({'product_id': '5', 'brand': 'Sony', 'rating': '4.8', 'price': '899'})
        
        result = read_csv_files([sample_csv_file, str(second_file)])
        
        assert len(result) == 5
    
    def test_read_empty_file(self, empty_csv_file):
        result = read_csv_files([empty_csv_file])
        
        assert len(result) == 0
    
    def test_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            read_csv_files(['non_existent_file.csv'])
    
    def test_file_with_different_data(self, tmp_path):
        different_file = tmp_path / "different.csv"
        with open(different_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['product_id', 'brand', 'rating'])
            writer.writeheader()
            writer.writerow({'product_id': '10', 'brand': 'LG', 'rating': '4.3'})
            writer.writerow({'product_id': '11', 'brand': 'Huawei', 'rating': '4.1'})
        
        result = read_csv_files([str(different_file)])
        
        assert len(result) == 2
        assert result[0]['brand'] == 'LG'
        assert result[1]['brand'] == 'Huawei'
