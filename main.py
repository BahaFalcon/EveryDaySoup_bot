import telebot
import bs4
import urllib
import random

site = urllib.request.urlopen('https://webspoon.ru/').read()
soup = bs4.BeautifulSoup(site)
#print(soup.prettify())

raw_recepts = soup.find('div', {"class":'CardGridNew'})
recepts = raw_recepts.find_all('a', {"class":'RecipeCardNew-imageLink'})
links_to_recepts = []

for i in recepts:
    links_to_recepts.append(i.get('href'))

print(links_to_recepts)
print('I have a list')
TOKEN = ' '
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def command_hello(message):
    bot.reply_to(message, "Привет! Я EveryDaySoup bot, могу помочь тебе найти рецепт блюд!")

@bot.message_handler(commands=['task'])
def send_task(message):
    link_to_send = random.choice(links_to_recepts)
    bot.reply_to(message, f'Окей, вот ингредиенты — {link_to_send}')

while True:
    bot.polling()