import requests
import json


query = input("What news you are looking for ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-05-17&sortBy=publishedAt&apiKey=152bd083f06c4ab583909198b5403f94"
r = requests.get(url)
print(r.text)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
  print(article["title"])
  print(article["description"])
  print("--------------------------------------")
