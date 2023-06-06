import requests

url = "https://mtgjson.com/api/v5/AtomicCards.json"
filename = "databases/AtomicCards.json"

response = requests.get(url)
response.raise_for_status()

with open(filename, "wb") as file:
    file.write(response.content)

print("File Updated Successfully")