from urllib.request import urlopen

with urlopen('http://www.dir.bg') as response:
    response_bytes = response.read()
    response_text = response_bytes.decode('utf-8')
    print(response_text)
