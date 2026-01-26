# vinst-p--lgh
Enkel Beräkning av Vinst På Lägenhet - Varning för glädje kalkyl

## Simple Apartment Sale Profit Calculator (Sweden)

A simple web application for calculating profit or loss when selling an apartment in Sweden.

## Features

- 🇸🇪 Swedish language interface
- 💰 Real-time profit/loss calculation
- 🎨 Clean, minimal design
- ♿ Accessible with screen reader support
- 📱 Mobile-responsive layout
- ✅ Input validation (prevents negative values)
- 🎨 Color-coded results (green for profit, red for loss)

## How to Use

1. Open `index.html` in your web browser
2. Enter your financial data:
   - **Försäljningspris** (Sale price)
   - **Inköpspris** (Purchase price)
   - **Renovering/Förbättringar** (Renovation/Improvements)
   - **Mäklararvode** (Broker fee)
   - **Årsavgifter** (Annual fees paid)
   - **Övriga kostnader** (Other costs)
3. The calculator will automatically show:
   - **Total kostnad** (Total cost)
   - **Vinst/Förlust** (Profit/Loss) - in green if profit, red if loss

## Running Locally

Simply open the `index.html` file in any modern web browser:

```bash
# Option 1: Direct file access
open index.html

# Option 2: Using Python's built-in HTTP server
python3 -m http.server 8080
# Then visit: http://localhost:8080/index.html
```

## Future Plans

- Mobile application (iOS/Android)
- Additional tax calculations
- Historical data storage
- Export to PDF
