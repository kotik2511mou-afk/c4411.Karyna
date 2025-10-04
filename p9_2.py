import requesets
response = requesets.get("https://httpbin.org/get")
print(response.text)

