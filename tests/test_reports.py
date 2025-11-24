import pytest
from src.reports.average_rating import AverageRatingReport

class TestAverageRatingReport:
    def test_calculate_average_rating(self, sample_csv_data, average_rating_report):
        result = average_rating_report.calculate(sample_csv_data)
        
        assert len(result) == 3
        
        apple_result = next(item for item in result if item['brand'] == 'Apple')
        assert apple_result['average_rating'] == 4.6
        
        assert result[0]['average_rating'] >= result[1]['average_rating']
        assert result[1]['average_rating'] >= result[2]['average_rating']
    
    def test_calculate_with_missing_ratings(self, average_rating_report):
        data_with_missing = [
            {'brand': 'Test1', 'rating': '4.5'},
            {'brand': 'Test2'},
            {'brand': 'Test3', 'rating': '3.5'},
            {'brand': 'Test1', 'rating': '4.0'},
        ]
        
        result = average_rating_report.calculate(data_with_missing)
        
        assert len(result) == 2
        brands = [item['brand'] for item in result]
        assert 'Test1' in brands
        assert 'Test3' in brands
        assert 'Test2' not in brands
    
    def test_calculate_empty_data(self, average_rating_report):
        result = average_rating_report.calculate([])
        
        assert result == []
    
    def test_display_method(self, average_rating_report, sample_csv_data, capsys):
        results = average_rating_report.calculate(sample_csv_data)
        
        average_rating_report.display(results)
        
        captured = capsys.readouterr()
        assert "Бренд" in captured.out
        assert "Средний рейтинг" in captured.out
    
    def test_generate_method(self, average_rating_report, sample_csv_data, capsys):
        average_rating_report.generate(sample_csv_data)
        
        captured = capsys.readouterr()
        assert "Бренд" in captured.out
        assert "Средний рейтинг" in captured.out
    
    def test_single_brand_calculation(self, average_rating_report):
        single_brand_data = [
            {'brand': 'Sony', 'rating': '4.8'},
            {'brand': 'Sony', 'rating': '4.9'},
            {'brand': 'Sony', 'rating': '4.7'},
        ]
        
        result = average_rating_report.calculate(single_brand_data)
        
        assert len(result) == 1
        assert result[0]['brand'] == 'Sony'
        assert result[0]['average_rating'] == 4.8
