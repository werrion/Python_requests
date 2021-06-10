import requests
data = requests.post ("https://petstore.swagger.io/v2/user/createWithList")
print(data.status_code)
assert data.status_code == 200


