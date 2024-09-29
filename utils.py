import requests
from datetime import datetime


def get_token_price_at_time(token_id, timestamp):
    date_str = timestamp.strftime('%d-%m-%Y')  # Format the timestamp for CoinGecko
    url = f'https://api.coingecko.com/api/v3/coins/{token_id}/history?date={date_str}'
    response = requests.get(url).json()
    return response['market_data']['current_price']['usd']


def calculate_profit_and_roi(transactions, current_price, wallet_address, get_token_price_at_time):
    total_investment = 0
    total_coins = 0

    for tx in transactions:
        value_in_ether = int(tx['value']) / (10 ** 18)  # Convert Wei to Ether
        tx_time = datetime.utcfromtimestamp(int(tx['timeStamp']))
        price_at_time = get_token_price_at_time('ethereum', tx_time)

        if tx['to'] == wallet_address.lower():
            # Buy
            total_investment += value_in_ether * price_at_time
            total_coins += value_in_ether
        elif tx['from'] == wallet_address.lower():
            # Sell
            total_investment -= value_in_ether * price_at_time
            total_coins -= value_in_ether

    # Current value
    current_value = total_coins * current_price

    # Profit
    profit = current_value - total_investment

    # ROI
    roi = (profit / total_investment) * 100 if total_investment != 0 else 0

    return profit, roi
