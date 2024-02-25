import requests

# Получение данных с сайта
response = requests.get('https://coinmarketcap.com/').text

# Разделение данных по тегу <span>
splitted_response = response.split("<span>")

for text in splitted_response:
    if text.startswith("$"):
        # убираем лишние данные
        for text2 in text.split("</span>"):
            if text2.startswith("$") and text2[1].isdigit():
                print(text2)
