import requests

# Define the API endpoint URL (JSONPlaceholder is a mock API for testing)
api_url = "https://jsonplaceholder.typicode.com/todos/1"

# Send a GET request to the URL and store the server's response
response = requests.get(url=api_url)

# Convert the raw response text into a Python dictionary and print it
print(response.json())

# Display the data type to verify it has been converted from a string to a dictionary
print(type(response.json())) # Output: <class 'dict'>

# Iterate through the dictionary to extract and print each key-value pair
# .items() is required to loop through both keys (labels) and values (data)
for key, value in response.json().items():
    print(key, value)
