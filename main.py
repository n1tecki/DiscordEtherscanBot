import discord
import os
from dotenv import load_dotenv
from etherscanio_utils import get_eth_transactions, get_erc20_transactions
from utils import get_token_price_at_time, calculate_profit_and_roi
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
ETHERSCAN_API_KEY = os.getenv('ETHERSCAN_API_KEY')


