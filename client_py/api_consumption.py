import requests as re

endpoint = "http://127.0.0.1:8000/api/song"

reqst = re.get(endpoint)
json_data = reqst.json()

print(json_data)