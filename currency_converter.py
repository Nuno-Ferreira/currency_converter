import os
import requests
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()
api_key = os.getenv("API_KEY")

# API Headers
headers= {"apikey": api_key}

# User Input Variables
currency_to_convert_to = str(input("Which currency would you like to convert to? "))
currency_to_convert_from = str(input("Which currency would you like to convert from? "))
amount_to_convert = int(input("How much would you like to convert? "))

def main():

  # API URL
  url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to_convert_to}&from={currency_to_convert_from}&amount={amount_to_convert}"

  # Request to get the converted currency
  response = requests.request("GET", url, headers=headers)

  if response.status_code != 200:
    print("Error: Unable to convert currency")
    return 1
  elif response.status_code == 429:
    print("API Limit Reached.")

  # Convert the response to JSON for easy parsing
  result = response.json()

  # Print the converted amount
  print(result["result"])

main()
