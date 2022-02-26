import requests

resp = requests.get("http://127.0.0.1:8000/Home_cbv/",)
print(resp.content)