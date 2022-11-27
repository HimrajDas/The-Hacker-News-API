import requests
import json

url = "https://hacker-news.firebaseio.com/v0/item/19155826.json"
# url = "https://hacker-news.firebaseio.com/v0/item/topstories.json"  --> This is for all the top stories of homepage.

r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.
response_dict = r.json()
readable_file = "readable_hn_data.json"
with open(readable_file, 'w') as file:
    json.dump(response_dict, file, indent=4)
