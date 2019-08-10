import requests
from bs4 import BeautifulSoup


print("""
    Choose your city:
    Athens --> 1
    Thessaloniki --> 2
    Patras --> 3  
    Heraklion --> 4  
""")

choice = int(input(">"))


def choice_maker(choice):
    switcher = {
        1: "12",
        2: "1",
        3: "10",
        4: "23"
        }
    return switcher.get(choice, "12")  # default for athens


result = choice_maker(choice)

URL = ("http://meteo.gr/cf-en.cfm?city_id="+str(result))

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")


def check_weather_clear():
    for table in soup.find_all("td", class_="phenomeno-name", limit=1):
        if (table.text[:5]) == "Clear":
            print(f"The weather is {table.text[:5]}")
        elif (table.text[:5]) == "Storm":
            print("The weather is Stormy")
        elif (table.text[:10]) == "Light Rain":
            print("The weather is Light Rain")
        elif (table.text[:4]) == "Rain":
            print("The weather is Rainy")
        else:
            pass


def check_weather_temperature():
    for weather in soup.find_all("td", class_="normal", limit=1):
        print(f"Current Temperature is {weather.text[:4]}.")


check_weather_temperature()
check_weather_clear()


