# vinst-p--lgh
Enkel Beräkning av Vinst På Lägenhet - Varning för glädje kalkyl

## Overview
This project provides tools for calculating profit on apartment (lägenhet/LGH) sales in Sweden. It generates formatted sale descriptions in TXT format, including detailed profit calculations and financial analysis.

## Features
- **LGH Sale Description Generator**: Create formatted TXT descriptions of apartment sales
- **Profit Calculation**: Automatically calculate gross and net profit
- **Financial Analysis**: Calculate annual return percentage and ownership duration
- **Swedish Language Support**: All descriptions are in Swedish
- **CLI Tool**: Easy-to-use command-line interface

## Installation
No external dependencies required. Just clone the repository and run with Python 3.7+:

```bash
git clone https://github.com/howcan66/vinst-p--lgh.git
cd vinst-p--lgh
```

## Usage

### As a Python Module
```python
from datetime import date
from lgh_sale import LGHSale

# Create a sale record
sale = LGHSale(
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
    description="Charmig 2:a med balkong i söderläge."
)

# Generate TXT description
print(sale.to_txt())

# Calculate profit metrics
print(f"Net profit: {sale.calculate_net_profit():,.0f} SEK")
print(f"Annual return: {sale.calculate_annual_return_percent()}%")
```

### Using the CLI Tool
```bash
python generate_sale_description.py \
  --address "Storgatan 15, 2tr, Stockholm" \
  --area 62.5 \
  --rooms 2 \
  --floor 2 \
  --purchase-price 2500000 \
  --purchase-date 2020-03-15 \
  --sale-price 3200000 \
  --sale-date 2024-11-20 \
  --monthly-fee 3850 \
  --renovation-costs 150000 \
  --description "Charmig 2:a med balkong" \
  --output sale_description.txt
```

### Running the Example
```bash
python lgh_sale.py
```

## Testing
Run the test suite:
```bash
python -m unittest test_lgh_sale.py -v
```

## Output Format
The TXT output includes:
- Property information (address, size, rooms, floor, monthly fee)
- Property description
- Financial details (purchase/sale dates and prices)
- Costs breakdown (broker fee, renovations)
- Profit calculation (gross/net profit, ownership duration, annual return)

### Example Output
```
============================================================
FÖRSÄLJNINGSBESKRIVNING - LÄGENHET
============================================================

FASTIGHETSINFORMATION:
  Adress: Storgatan 15, 2tr, 123 45 Stockholm
  Storlek: 62.5 m²
  Antal rum: 2
  Våning: 2
  Månadskostnad: 3,850 SEK

EKONOMISK INFORMATION:
  Köpdatum: 2020-03-15
  Köpeskilling: 2,500,000 SEK
  Försäljningsdatum: 2024-11-20
  Försäljningspris: 3,200,000 SEK

KOSTNADER:
  Mäklarprovision (2.0%): 64,000 SEK
  Renoveringskostnader: 150,000 SEK

VINSTBERÄKNING:
  Bruttovinst: 700,000 SEK
  Nettovinst: 486,000 SEK
  Ägandets längd: 4.7 år
  Årlig avkastning: 4.14%
```

## License
MIT
