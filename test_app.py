import requests

url_addr = 'http://127.0.0.1:5000/predict'
res = requests.post(url_addr, json={"data":"-PLS STOP bootydelious (32/F) is inviting you "})
print (res.status_code)
print(res.json())