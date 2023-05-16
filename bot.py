import os
import telebot
import requests
import json
import csv
from dotenv import load_dotenv
load_dotenv()

# TODO: 1.1 Get your environment variables
your_key = os.getenv('your_key')
bot_id = os.getenv('bot_id')

bot = telebot.TeleBot(bot_id)

botRunning = False
movie_data = []

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')

@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')

@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')

@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    global movie_data
    bot.reply_to(message, 'Getting movie info...')
    movie_name = message.text.split(' ', 1)[1]
    omdb_url = f'http://www.omdbapi.com/?t={movie_name}&apikey={your_key}'
    response = requests.get(omdb_url)
    movie_json = json.loads(response.text)
    if movie_json['Response'] == 'False':
        bot.reply_to(message, 'Sorry, I could not find any information for that movie.')
    else:
        title = movie_json["Title"]
        year = movie_json["Year"]
        director = movie_json["Director"]
        imdb_rating = movie_json["imdbRating"]
        movie_data.append({'title': title, 'year': year, 'director': director, 'imdb_rating': imdb_rating})
        bot.reply_to(message, f'Title: {title}\nYear: {year}\nDirector: {director}\nIMDB Rating: {imdb_rating}')
        # TODO: 2.1 Create a CSV file and dump the movie information in it
        with open('movies.csv', 'w', newline='') as csvfile:
            fieldnames = ['title', 'year', 'director', 'imdb_rating']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for movie in movie_data:
                writer.writerow({'title': movie['title'], 'year': movie['year'], 'director': movie['director'], 'imdb_rating': movie['imdb_rating']})

@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    global movie_data
    bot.reply_to(message, 'Generating file...')
    # TODO: 2.2 Send downloadable CSV file to telegram chat
    with open('movies.csv', 'rb') as csvfile:
        bot.send_document(message.chat.id, csvfile)
    movie_data = []

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')

bot.infinity_polling()