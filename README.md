# 💱 Currency Converter Real-Time

A terminal-based Python application that converts currencies using **live exchange rates** from the ExchangeRate API. Always up-to-date, no manual rate input needed.

---

## 🚀 Features

- ✅ Real-time exchange rates from ExchangeRate API
- ✅ Support for 150+ world currencies
- ✅ Automatic uppercase conversion (usd → USD)
- ✅ Displays exchange rate and last update timestamp
- ✅ Convert multiple currencies without restarting
- ✅ Input validation with error handling
- ✅ Clean formatted output with emoji indicators

---

## 📸 Preview

```
=== Currency Converter Real-Time ===
Enter amount: 100
From currency (e.g. USD, IDR): USD
To currency (e.g. IDR, JPY): IDR

🔄 Fetching latest exchange rates...

========================================
💰 Conversion Result: 100.00 USD = 1,788,501.00 IDR
📈 Exchange Rate    : 1 USD = 17,885.0100 IDR
🕒 Last Updated     : 2026-06-29 07:00:01
========================================

Convert again? (y/n): y
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.x |
| HTTP Client | requests |
| API | ExchangeRate-API (free tier) |
| Libraries | `requests`, `datetime` |
| Interface | Terminal / Command Line |

---

## ⚙️ How to Use

**1. Clone this repository:**
```bash
git clone https://github.com/aryawirawicaksana029-ui/currency_converter.git
cd currency_converter
```

**2. Install dependencies:**
```bash
pip install requests
```

**3. Run the program:**
```bash
python currency_converter.py
```

**4. Follow the prompts:**
```
Enter amount        → e.g. 100
From currency       → e.g. USD
To currency         → e.g. IDR, EUR, JPY
```

---

## 🌍 Supported Currencies (Sample)

| Code | Currency |
|------|----------|
| USD | US Dollar |
| IDR | Indonesian Rupiah |
| EUR | Euro |
| JPY | Japanese Yen |
| SGD | Singapore Dollar |
| GBP | British Pound |
| AUD | Australian Dollar |
| MYR | Malaysian Ringgit |

And 140+ more currencies supported!

---

## 📊 How It Works

```
User Input (amount, from, to)
        ↓
GET https://api.exchangerate-api.com/v4/latest/{from_currency}
        ↓
Parse JSON Response
        ↓
Calculate: amount × exchange_rate
        ↓
Display Result with timestamp
```

---

## 📁 Project Structure

```
currency-converter/
│
├── currency_converter.py   # Main program
└── README.md               # Project documentation
```

---

## 👨‍💻 Author

**Arya Wira Wicaksana**
🐍 Python Developer | AI Enthusiast
📧 aryawirawicaksana029@gmail.com
🔗 [GitHub](https://github.com/aryawirawicaksana029-ui)

---

## 🔮 Future Plans

- [ ] GUI version with Tkinter
- [ ] Web App version with Flask
- [ ] Historical exchange rate chart
- [ ] Favorite currency pairs
- [ ] Offline mode with cached rates
- [ ] Multi-currency conversion at once
