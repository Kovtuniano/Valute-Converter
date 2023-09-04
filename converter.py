import requests

def currency_converter(amount, from_currency, to_currency):
    # API
    url = f"https://api.example.com/convert?from={from_currency}&to={to_currency}&amount={amount}"
    
    try:
        response = requests.get(url)
        data = response.json()
        converted_amount = data['converted_amount']
        return converted_amount
    except Exception as e:
        return f"Error: {str(e)}"

# Main
print("Enter amount to convert... ")
amount = input()  # Amout
print("Enter the original currency in caps, for example USD, UAH... ")
from_currency = input()  #Original
print("Enter the target currency in Caps, for example USD, UAH...")
to_currency = input()  # Target 

result = currency_converter(amount, from_currency, to_currency)
if isinstance(result, float):
    print(f"{amount} {from_currency} = {result} {to_currency}")
else:
    print(result)
