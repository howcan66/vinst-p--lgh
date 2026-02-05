"""
Tests for LGH Sale Description Generator
"""

import unittest
from datetime import date
from lgh_sale import LGHSale, create_example_sale


class TestLGHSale(unittest.TestCase):
    """Test cases for LGHSale class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.sale = LGHSale(
            address="Testgatan 1",
            area_sqm=50.0,
            rooms=2,
            floor=3,
            purchase_price=2_000_000,
            purchase_date=date(2020, 1, 1),
            sale_price=2_500_000,
            sale_date=date(2024, 1, 1),
            monthly_fee=3_000,
            renovation_costs=100_000,
            broker_fee_percent=2.0
        )
    
    def test_calculate_profit(self):
        """Test profit calculation."""
        self.assertEqual(self.sale.calculate_profit(), 500_000)
    
    def test_calculate_net_profit(self):
        """Test net profit calculation."""
        # Sale price: 2,500,000
        # Purchase price: 2,000,000
        # Gross profit: 500,000
        # Broker fee (2%): 50,000
        # Renovation: 100,000
        # Net profit: 500,000 - 50,000 - 100,000 = 350,000
        self.assertEqual(self.sale.calculate_net_profit(), 350_000)
    
    def test_calculate_ownership_years(self):
        """Test ownership years calculation."""
        self.assertEqual(self.sale.calculate_ownership_years(), 4.0)
    
    def test_calculate_annual_return(self):
        """Test annual return percentage calculation."""
        # Net profit: 350,000
        # Purchase price: 2,000,000
        # Total return: 17.5%
        # Annual return: 17.5% / 4 years = 4.375% per year
        self.assertEqual(self.sale.calculate_annual_return_percent(), 4.38)
    
    def test_to_txt_contains_key_information(self):
        """Test that TXT output contains all key information."""
        txt = self.sale.to_txt()
        
        # Check that key information is present
        self.assertIn("Testgatan 1", txt)
        self.assertIn("50.0 m²", txt)
        self.assertIn("2,000,000 SEK", txt)
        self.assertIn("2,500,000 SEK", txt)
        self.assertIn("350,000 SEK", txt)  # Net profit
        self.assertIn("4.0 år", txt)  # Ownership years
        self.assertIn("4.38%", txt)  # Annual return
    
    def test_to_txt_format(self):
        """Test that TXT output is properly formatted."""
        txt = self.sale.to_txt()
        
        # Check for section headers
        self.assertIn("FÖRSÄLJNINGSBESKRIVNING", txt)
        self.assertIn("FASTIGHETSINFORMATION:", txt)
        self.assertIn("EKONOMISK INFORMATION:", txt)
        self.assertIn("KOSTNADER:", txt)
        self.assertIn("VINSTBERÄKNING:", txt)
    
    def test_optional_fields(self):
        """Test sale without optional fields."""
        minimal_sale = LGHSale(
            address="Minigatan 1",
            area_sqm=30.0,
            rooms=1,
            floor=1,
            purchase_price=1_000_000,
            purchase_date=date(2022, 1, 1),
            sale_price=1_100_000,
            sale_date=date(2024, 1, 1)
        )
        
        txt = minimal_sale.to_txt()
        self.assertIsInstance(txt, str)
        self.assertIn("Minigatan 1", txt)
    
    def test_create_example_sale(self):
        """Test that example sale creation works."""
        example = create_example_sale()
        self.assertIsInstance(example, LGHSale)
        self.assertIsInstance(example.to_txt(), str)
    
    def test_broker_fee_none(self):
        """Test that broker_fee_percent=None is handled correctly."""
        sale_no_fee = LGHSale(
            address="Test",
            area_sqm=50.0,
            rooms=2,
            floor=1,
            purchase_price=1_000_000,
            purchase_date=date(2022, 1, 1),
            sale_price=1_100_000,
            sale_date=date(2024, 1, 1),
            broker_fee_percent=None
        )
        # Should not raise an error
        net_profit = sale_no_fee.calculate_net_profit()
        self.assertEqual(net_profit, 100_000)  # No broker fee deducted
        
        # TXT generation should also work
        txt = sale_no_fee.to_txt()
        self.assertIn("0.0%", txt)


if __name__ == "__main__":
    unittest.main()
