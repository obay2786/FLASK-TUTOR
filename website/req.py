import requests

while True:
    r = requests.get("https://newsapi.org/v2/top-headlines?apiKey=25ff185c903e49ddba06551850241e06&country=id")

    print(r.json())