import requests

endpoint = "http://localhost:8000/api/"

# Provide both title and content fields in the JSON payload
data = {
    'title': "1 Hello World!!",
    'content': "This is the content."

}

# Send the POST request with the correct JSON payload
get_response = requests.post(endpoint, json=data)

# Print the response content and status code
print(get_response.text)
print(get_response.status_code)
