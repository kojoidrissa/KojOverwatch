from bs4 import BeautifulSoup
import requests
ow = requests.get('https://worldcup.playoverwatch.com/en-us/')
ow_soup = BeautifulSoup(ow.text, 'html.parser')
print(ow_soup.prettify())
