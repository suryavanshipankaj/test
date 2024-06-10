import requests
from bs4 import BeautifulSoup

# Enter the City Name
city = input("Enter the City Name: ")
search = f"Weather in {city}"

# URL
url = f"https://www.google.com/search?q={search}"

# Sending HTTP request
req = requests.get(url)

# Pulling HTTP data from internet
sor = BeautifulSoup(req.text, "html.parser")

# Finding temperature in Celsius
temp = sor.find("div", class_='BNeawe').text

print(f'Temperature in {city} is {temp}')
