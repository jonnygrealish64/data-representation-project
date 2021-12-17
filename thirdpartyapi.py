import requests
import json

url = "https://www.psnleaderboard.com/api/"
response = requests.get(url)
data = response.json()

filename = 'hoffjagerpsnprofile.json'
f = open(filename, 'w')
json.dump(data, f, indent = 4)