import requests
import random

# Authorization token
token = "0222f37843ae89a63abc1eff3601b030c3d4e238"
headers = {"Authorization": f"Bearer {token}"}

# API endpoint
endpoint = "http://localhost:8000/api/products/"

# Define lists of possible titles, contents, and prices
titles = ["Lorem Ipsum", "Random Title", "Test Product"]
contents = ["Lorem ipsum dolor sit amet.", "Random content for testing."]
prices = [13.24, 234.45, 523.23, 56.34]

# Generate random data for each request
data = {
    'title': random.choice(titles),
    'content': random.choice(contents),
    'price': random.choice(prices),
}

# Send the POST request with the generated JSON payload
response = requests.post(endpoint, headers=headers, json=data)

# Print the response content and status code
print(response.json())
print(response.status_code)
