import requests
import json #dump, dumps, load, loads
from pprint import pprint

# # GET requests with incorrect postcode example.
# r = requests.get("https://api.postcodes.io/postcodes/SEA190")
#
# print(r, type(r))
# print(r.status_code)
# # print(r.headers, type(r.headers)) # headers is in dictionary format
# # print(r.headers['Date'])
#
# if r.status_code == 200:
#     content = r.content
#     # print(content, type(content))
#     content_json = r.json()
#     # print(content_json, type(content_json))
#
# # Print the eastings and northings for this postcode
#
# result_content = content_json['result']
# eastings = result_content['eastings']
# northings = result_content['northings']
# print("Eastings:", eastings, ", Northings:", northings)

# headers = {"Content-Type": "application/json"}
# data = json.dumps({"postcodes": ["OX49 5NU", "M32 0JG", "NE30 1DP"]})
#
#
# r = requests.post(
#     url="https://api.postcodes.io/postcodes",
#     headers=headers,
#     data=data
# )

# Above codes shows what happens under the hood; below is a shorthand for
# handling data into a JSON format.

headers = {"Content-Type": "application/json"}
data = {"postcodes": ["OX49 5NU", "M32 0JG", "NE30 1DP"]}


r = requests.post(
    url="https://api.postcodes.io/postcodes",
    headers=headers,
    json=data
)
# print(r)
print(r.json()['status'])


# For each postcode, print POSTCODE: region, parlimentary_constituency
result_list = r.json()['result']
print(type(result_list))

for result in result_list:
    print(result.get('query') + ":",
          result['result'].get('region') + ",",
          result['result'].get('parliamentary_constituency'))