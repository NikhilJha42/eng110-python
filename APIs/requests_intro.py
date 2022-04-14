import requests

r = requests.get("http://www.bbc.com")

print(r, type(r))