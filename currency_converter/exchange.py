import requests

# URL API для отримання курсів валют
API_URL = "https://api.exchangerate-api.com/v4/latest/"

def get_exchange_rate(base_currency, target_currency):
    """Отримує курс обміну між двома валютами."""
    response = requests.get(f"{API_URL}{base_currency}")
    data = response.json()
    
    if response.status_code != 200:
        raise Exception("Error fetching exchange rate data.")
    
    if target_currency not in data['rates']:
        raise Exception(f"Target currency {target_currency} not supported.")
    
    return data['rates'][target_currency]

def convert_amount(base_currency, target_currency, amount):
    """Конвертує суму з однієї валюти в іншу."""
    rate = get_exchange_rate(base_currency, target_currency)
    return round(amount * rate, 2)

def get_supported_currencies():
    """Отримує список підтримуваних валют."""
    response = requests.get(f"{API_URL}USD")
    data = response.json()
    
    if response.status_code != 200:
        raise Exception("Error fetching currencies data.")
    
    return list(data['rates'].keys())
