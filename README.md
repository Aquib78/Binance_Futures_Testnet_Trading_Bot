# Binance Futures Testnet Trading Bot

## Overview

This project is a Python-based Trading Bot developed for Binance Futures Testnet (USDT-M). The application allows users to place Market and Limit orders through a Command Line Interface (CLI) with proper input validation, logging, and error handling.

## Features

* Place MARKET orders
* Place LIMIT orders
* Support BUY and SELL order sides
* Command-line interface using Click
* Input validation
* Error handling for invalid inputs and API errors
* Logging of requests, responses, and errors
* Binance Futures Testnet integration

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   └── cli.py
│
├── logs/
│   └── trading.log
│
├── .env
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

## Prerequisites

* Python 3.9+
* Binance Futures Testnet Account
* Binance Futures Testnet API Key and Secret

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd trading_bot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_api_secret
```

## Binance Futures Testnet

Generate API credentials from:

https://testnet.binancefuture.com

Do not use production Binance API keys.

## Running the Application

### MARKET Order Example

```bash
python main.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.001
```

### LIMIT Order Example

```bash
python main.py --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.001 --price 200000
```

## CLI Parameters

| Parameter  | Description                  | Required       |
| ---------- | ---------------------------- | -------------- |
| symbol     | Trading pair (e.g., BTCUSDT) | Yes            |
| side       | BUY or SELL                  | Yes            |
| order_type | MARKET or LIMIT              | Yes            |
| quantity   | Order quantity               | Yes            |
| price      | Limit order price            | Only for LIMIT |

## Logging

Logs are stored in:

```text
logs/trading.log
```

The log file records:

* Order requests
* Order responses
* Errors and exceptions

## Validation

The application validates:

* Order side (BUY/SELL)
* Order type (MARKET/LIMIT)
* Required parameters for LIMIT orders

## Error Handling

The application handles:

* Invalid user input
* Binance API errors
* Network-related exceptions
* Missing parameters

## Assumptions

* User has a valid Binance Futures Testnet account.
* Testnet API credentials are configured correctly.
* Internet connection is available.
* Trading is performed only on Binance Futures Testnet.

## Sample Output

```text
----- ORDER REQUEST -----
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

----- ORDER RESPONSE -----
Order ID: 13686593445
Status: NEW
Executed Qty: 0.0000

✓ Order placed successfully
```

## Author

Md Aquib Hussain

B.Tech Robotics and Automation

REVA University
