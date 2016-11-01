import requests

TARGET_URL = 'http://www.dir.bg'
IMAGE_TAG = '<img '
response = requests.get(TARGET_URL)

# print(response.status_code)
# print(response.text)
# print(response.json())

response_text = response.text


if IMAGE_TAG in response_text:
    print("Има картинки")

count = 0
found_index = 0
while found_index != -1:
    found_index = response_text.find(IMAGE_TAG, found_index)
    if found_index != -1:
        count += 1
        found_index += 1

print("{} images found on th page: {}". format(
    count,
    TARGET_URL
))
