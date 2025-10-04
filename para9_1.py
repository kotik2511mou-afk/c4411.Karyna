import urllib.request

opener = urllib.request.build_opener()
respons = opener.open("https://httpbin.org/get")
print(respons.read)
