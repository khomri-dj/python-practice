import requests
respon=requests.get("https://jsonplaceholder.typicode.com/users")

print(respon.status_code)

users=respon.json()
for user in users:
    print(user["name"])
    print(user["email"])
    print("______________________")