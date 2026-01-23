import requests

# Step 1: Your personal password (API Key) to access the stock data
API_key = "17VNXABFEF6HF03S" 

# Step 2: The main website address (Base URL) we are getting data from
API_url = "https://www.alphavantage.co" 

# Create a function that asks the website for specific stock info
def get_stock_market_data(symbol):
    # Step 3: Combine the settings (Stock name and API Key) into a specific request
    query = f"/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_key}" 
    
    # Send the request to the internet and get the answer
    response = requests.get(url=API_url + query)
    
    # Convert the answer into a format Python can read (JSON) and print it
    print(response.json())
    
# Step 4: Ask the user to type a stock name (like GOGL for google or AMZN for Amazon)
symbol = input("Enter the stock symbol (e.g., AMZN, GOOGL, IBM): ")

# Step 5: Run the function with the name the user typed in
get_stock_market_data(symbol)
