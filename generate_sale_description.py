#!/usr/bin/env python3
"""
CLI tool for generating LGH (apartment) sale descriptions in TXT format.
"""

import argparse
from datetime import datetime
from lgh_sale import LGHSale


def parse_date(date_str):
    """Parse a date string in YYYY-MM-DD format."""
    return datetime.strptime(date_str, "%Y-%m-%d").date()


def main():
    parser = argparse.ArgumentParser(
        description="Generate apartment sale description in TXT format"
    )
    
    # Required arguments
    parser.add_argument("--address", required=True, help="Property address")
    parser.add_argument("--area", type=float, required=True, help="Area in square meters")
    parser.add_argument("--rooms", type=int, required=True, help="Number of rooms")
    parser.add_argument("--floor", type=int, required=True, help="Floor number")
    parser.add_argument("--purchase-price", type=float, required=True, help="Purchase price in SEK")
    parser.add_argument("--purchase-date", type=parse_date, required=True, help="Purchase date (YYYY-MM-DD)")
    parser.add_argument("--sale-price", type=float, required=True, help="Sale price in SEK")
    parser.add_argument("--sale-date", type=parse_date, required=True, help="Sale date (YYYY-MM-DD)")
    
    # Optional arguments
    parser.add_argument("--monthly-fee", type=float, help="Monthly fee in SEK")
    parser.add_argument("--renovation-costs", type=float, help="Renovation costs in SEK")
    parser.add_argument("--broker-fee", type=float, default=2.0, help="Broker fee percentage (default: 2.0)")
    parser.add_argument("--description", help="Property description")
    parser.add_argument("--output", "-o", help="Output file (default: print to stdout)")
    
    args = parser.parse_args()
    
    # Create LGHSale object
    sale = LGHSale(
        address=args.address,
        area_sqm=args.area,
        rooms=args.rooms,
        floor=args.floor,
        purchase_price=args.purchase_price,
        purchase_date=args.purchase_date,
        sale_price=args.sale_price,
        sale_date=args.sale_date,
        monthly_fee=args.monthly_fee,
        renovation_costs=args.renovation_costs,
        broker_fee_percent=args.broker_fee,
        description=args.description
    )
    
    # Generate TXT output
    txt_output = sale.to_txt()
    
    # Write to file or print to stdout
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(txt_output)
        print(f"Sale description saved to {args.output}")
    else:
        print(txt_output)


if __name__ == "__main__":
    main()
