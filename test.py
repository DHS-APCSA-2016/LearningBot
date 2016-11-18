import requests
import json

r = requests.post("http://localhost:5000/", json={"input": "hi"})