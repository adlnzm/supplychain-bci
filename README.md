# Blockchain-Integrated Supply Chain Management: Price Prediction Module

````markdown

This project showcases a blockchain-integrated approach to supply chain transparency and decision-making using cryptocurrency price predictions. It combines Ethereum smart contracts with a machine learning model served through a Flask API to predict cryptocurrency prices and log predictions on-chain for transparency.

---

## Project Overview

The system allows users to:
- Predict cryptocurrency prices using a trained Random Forest machine learning model.
- Store and retrieve price predictions on a public Ethereum blockchain via a smart contract.
- Demonstrate transparency and auditability in predictive analytics for financial supply chains.

---

## Tech Stack

- **Smart Contract**: Solidity (Ethereum)
- **Backend API**: Flask (Python)
- **Machine Learning**: Scikit-learn (RandomForestRegressor)
- **Data Processing**: Pandas
- **Blockchain Interaction**: Web3 (can be integrated separately with web3.py or Web3.js)

---

## Dataset Description

The machine learning model is trained using historical cryptocurrency data sourced from [CoinGecko](https://www.coingecko.com/), split across two files:

- `coin_gecko_2022-03-16.csv`
- `coin_gecko_2022-03-17.csv`

### Dataset Fields:
| Column Name       | Description                                      |
|-------------------|--------------------------------------------------|
| `coin`            | Name of the cryptocurrency (e.g., BTC, ETH)     |
| `date`            | Date of the record (YYYY-MM-DD format)          |
| `price`           | Closing price of the cryptocurrency             |
| `mkt_cap`         | Market capitalization in USD                    |
| `volume`          | Trading volume in USD                           |
| `price_change_24h`| (Engineered) % price change over previous day   |
| `mkt_cap_change_24h`| (Engineered) % market cap change over 24 hrs  |
| `price_lag_1`     | (Engineered) Previous day's price               |
| `mkt_cap_lag_1`   | (Engineered) Previous day's market cap          |

After cleaning and processing:
- Missing values are dropped
- Data is sorted by `coin` and `date`
- Lag features and percentage changes are calculated for model inputs

These features help predict the future price of a given coin.

---

## Smart Contract – `PricePrediction.sol`

The `PricePrediction` smart contract stores user predictions on the Ethereum blockchain.

### Key Features:
- `storePrediction(coin, predictedPrice)`: Stores a new prediction.
- `getTotalPredictions()`: Returns the total number of predictions.
- `PredictionLogged`: Event emitted for every new prediction.

---

## Machine Learning API – `flask_web3.py`

The Flask backend serves as a RESTful API for price prediction using a RandomForestRegressor model.

### API Endpoint

`POST /predict`

#### Sample Request:
```json
{
  "price_lag_1": 40000,
  "mkt_cap_lag_1": 750000000,
  "price_change_24h": 0.02,
  "mkt_cap_change_24h": 0.015
}
````

#### Sample Response:

```json
{
  "predicted_price": 40750.34
}
```

## Installation & Setup

### Prerequisites:

* Python 3.8+
* Flask
* Scikit-learn
* Pandas
* Node.js & Hardhat (for contract deployment)
* MetaMask / Ethereum wallet (for interaction)

### Backend Setup:

```bash
# Clone the repository
git clone https://github.com/yourusername/blockchain-supplychain-price-prediction.git
cd blockchain-supplychain-price-prediction

# Set up Python environment
pip install -r requirements.txt

# Run Flask API
python flask_web3.py
```

## File Structure

```
.
├── PricePrediction.sol         # Ethereum smart contract
├── flask_web3.py              # Flask app with ML model
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── /data
│   ├── coin_gecko_2022-03-16.csv
│   └── coin_gecko_2022-03-17.csv
```

## Use Cases

* **Supply Chain Finance**: Transparent price forecasts for better procurement strategies.
* **Crypto Logistics**: Coin-based pricing estimations for shipment insurance or tokenized commodity trades.
* **Forecast Auditing**: Immutable record of all predictions for retrospective analysis.
