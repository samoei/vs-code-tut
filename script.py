import requests

r = requests.get("http://www.samphiltech.com/")
print(r.status_code)
