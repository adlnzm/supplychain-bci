import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from flask import Flask, request, jsonify

# Load the datasets
file_path_1 = "/Users/adlnzmnzr/Downloads/archive/coin_gecko_2022-03-16.csv"
file_path_2 = "/Users/adlnzmnzr/Downloads/archive/coin_gecko_2022-03-17.csv"

df1 = pd.read_csv(file_path_1)
df2 = pd.read_csv(file_path_2)

# Merge datasets
df = pd.concat([df1, df2])

# Drop rows with missing values
df_cleaned = df.dropna()

# Convert date to datetime format
df_cleaned['date'] = pd.to_datetime(df_cleaned['date'])

# Sort data by coin and date
df_cleaned = df_cleaned.sort_values(by=['coin', 'date'])

# Feature Engineering
df_cleaned['price_lag_1'] = df_cleaned.groupby('coin')['price'].shift(1)
df_cleaned['mkt_cap_lag_1'] = df_cleaned.groupby('coin')['mkt_cap'].shift(1)
df_cleaned['price_change_24h'] = df_cleaned.groupby('coin')['price'].pct_change()
df_cleaned['mkt_cap_change_24h'] = df_cleaned.groupby('coin')['mkt_cap'].pct_change()

# Drop NaN values after feature creation
df_features = df_cleaned.dropna()

# Define features and target
X = df_features[['price_lag_1', 'mkt_cap_lag_1', 'price_change_24h', 'mkt_cap_change_24h']]
y = df_features['price']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestRegressor model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Flask WSGI Server
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = [data['price_lag_1'], data['mkt_cap_lag_1'], data['price_change_24h'], data['mkt_cap_change_24h']]
    prediction = model.predict([features])[0]
    return jsonify({'predicted_price': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
