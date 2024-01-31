import requests

endpoint = "http://localhost:8000/api/products/4/update/"

# Provide both title and content fields in the JSON payload
data = {
    'title': "Data Updated",
    'content': "This is the content.",
    'price': 10000
}

# Send the POST request with the correct JSON payload
get_response = requests.put(endpoint, json=data)

# Print the response content and status code
print(get_response.text)
print(get_response.status_code)
