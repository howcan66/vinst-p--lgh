"""
LGH (Lägenhet/Apartment) Sale Description Generator

This module provides functionality to create and format apartment sale descriptions
in TXT format, including profit calculation capabilities.
"""

from dataclasses import dataclass
from typing import Optional
from datetime import date


@dataclass
class LGHSale:
    """Represents an apartment (lägenhet) sale with all relevant details."""
    
    # Basic property information
    address: str
    area_sqm: float
    rooms: int
    floor: int
    
    # Financial information
    purchase_price: float
    purchase_date: date
    sale_price: float
    sale_date: date
    
    # Optional details
    monthly_fee: Optional[float] = None
    renovation_costs: Optional[float] = None
    broker_fee_percent: Optional[float] = 2.0
    description: Optional[str] = None
    
    def calculate_profit(self) -> float:
        """Calculate the profit from the sale."""
        return self.sale_price - self.purchase_price
    
    def calculate_net_profit(self) -> float:
        """Calculate net profit after deducting costs."""
        gross_profit = self.calculate_profit()
        broker_fee_percent = self.broker_fee_percent or 0.0
        broker_fee = self.sale_price * (broker_fee_percent / 100)
        renovation = self.renovation_costs or 0.0
        return gross_profit - broker_fee - renovation
    
    def calculate_ownership_years(self) -> float:
        """Calculate the number of years the property was owned."""
        days_owned = (self.sale_date - self.purchase_date).days
        return round(days_owned / 365.25, 1)
    
    def calculate_annual_return_percent(self) -> float:
        """Calculate the annual return percentage."""
        years = self.calculate_ownership_years()
        if years == 0:
            return 0.0
        net_profit = self.calculate_net_profit()
        total_return_percent = (net_profit / self.purchase_price) * 100
        return round(total_return_percent / years, 2)
    
    def to_txt(self) -> str:
        """Generate a formatted TXT description of the apartment sale."""
        lines = []
        
        # Header
        lines.append("=" * 60)
        lines.append("FÖRSÄLJNINGSBESKRIVNING - LÄGENHET")
        lines.append("=" * 60)
        lines.append("")
        
        # Property details
        lines.append("FASTIGHETSINFORMATION:")
        lines.append(f"  Adress: {self.address}")
        lines.append(f"  Storlek: {self.area_sqm} m²")
        lines.append(f"  Antal rum: {self.rooms}")
        lines.append(f"  Våning: {self.floor}")
        if self.monthly_fee:
            lines.append(f"  Månadskostnad: {self.monthly_fee:,.0f} SEK")
        lines.append("")
        
        # Description
        if self.description:
            lines.append("BESKRIVNING:")
            lines.append(f"  {self.description}")
            lines.append("")
        
        # Financial details
        lines.append("EKONOMISK INFORMATION:")
        lines.append(f"  Köpdatum: {self.purchase_date.strftime('%Y-%m-%d')}")
        lines.append(f"  Köpeskilling: {self.purchase_price:,.0f} SEK")
        lines.append(f"  Försäljningsdatum: {self.sale_date.strftime('%Y-%m-%d')}")
        lines.append(f"  Försäljningspris: {self.sale_price:,.0f} SEK")
        lines.append("")
        
        # Costs
        lines.append("KOSTNADER:")
        broker_fee_percent = self.broker_fee_percent or 0.0
        broker_fee = self.sale_price * (broker_fee_percent / 100)
        lines.append(f"  Mäklarprovision ({broker_fee_percent}%): {broker_fee:,.0f} SEK")
        if self.renovation_costs:
            lines.append(f"  Renoveringskostnader: {self.renovation_costs:,.0f} SEK")
        lines.append("")
        
        # Profit calculation
        lines.append("VINSTBERÄKNING:")
        gross_profit = self.calculate_profit()
        net_profit = self.calculate_net_profit()
        ownership_years = self.calculate_ownership_years()
        annual_return = self.calculate_annual_return_percent()
        
        lines.append(f"  Bruttovinst: {gross_profit:,.0f} SEK")
        lines.append(f"  Nettovinst: {net_profit:,.0f} SEK")
        lines.append(f"  Ägandets längd: {ownership_years} år")
        lines.append(f"  Årlig avkastning: {annual_return}%")
        lines.append("")
        
        # Footer
        lines.append("=" * 60)
        
        return "\n".join(lines)


def create_example_sale() -> LGHSale:
    """Create an example apartment sale for demonstration purposes."""
    return LGHSale(
        address="Storgatan 15, 2tr, 123 45 Stockholm",
        area_sqm=62.5,
        rooms=2,
        floor=2,
        purchase_price=2_500_000,
        purchase_date=date(2020, 3, 15),
        sale_price=3_200_000,
        sale_date=date(2024, 11, 20),
        monthly_fee=3_850,
        renovation_costs=150_000,
        broker_fee_percent=2.0,
        description="Charmig 2:a med balkong i söderläge. Renoverad med nya golv och fräscht kök."
    )


if __name__ == "__main__":
    # Example usage
    sale = create_example_sale()
    print(sale.to_txt())
