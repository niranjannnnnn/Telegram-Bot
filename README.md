<h2>Movie Information Bot</h2>
This is a Python script that implements a Telegram bot to retrieve movie information using the OMDb API and export the data to a CSV file. The bot allows users to interact with it using various commands.

<h3>Prerequisites</h3>
Python 3.x
telebot library
requests library
json library
csv library
python-dotenv library

<h3>Setup</h3>

1. Clone the repository or download the script file (movie_bot.py)
2. Install the required dependencies by running the following command:

``` 
pip install -r requirements.txt
```

3. Obtain an API key from OMDb API. Sign up and get your personal API key.
4. Create a .env file in the same directory as the script and add the following environment variables:

```
your_key=YOUR_OMDB_API_KEY
bot_id=YOUR_TELEGRAM_BOT_TOKEN
```
Replace YOUR_OMDB_API_KEY with your actual OMDb API key, and YOUR_TELEGRAM_BOT_TOKEN with your Telegram bot token obtained from BotFather.

<h3>Usage</h3>

1. Start the bot by running the script:

```
python movie_bot.py
```

2. Open the Telegram app and search for your bot.
3. Send one of the available commands to the bot to interact with it:

   - '/start or /hello: Initiates a conversation with the bot.'
   
   - '/stop or /bye: Stops the bot and ends the conversation.'
   
   - '/help: Provides information on how to use the bot.'
   
   - '/movie MOVIE_NAME: Retrieves details of the specified movie. Replace MOVIE_NAME with the actual name of the movie.'
   
   - '/export: Exports all the retrieved movie data as a CSV file and sends it to the chat.'

<h3>Functionality</h3>

   - The bot interacts with the user through Telegram commands.
    
   - When the /start or /hello command is issued, the bot greets the user and becomes active.
   
   - When the /stop or /bye command is issued, the bot stops running and says goodbye.
    
   - The /help command provides instructions on how to use the bot.
    
   - The /movie MOVIE_NAME command retrieves movie information from the OMDb API based on the specified movie name. The details include the title, year, director, and IMDb rating. The retrieved    data is also stored in memory.
    
   - The /export command exports all the movie data retrieved so far as a CSV file and sends it to the chat.
    
   - The bot can handle unrecognized commands and responds with a default message.
   
<h3>Data Persistence</h3>
  
   - The movie data retrieved from the OMDb API is stored in memory as a list of dictionaries.
   
   - When the /export command is issued, the movie data is written to a CSV file named movies.csv.
   
   - The CSV file is sent to the chat as a downloadable document.
   
   - After exporting the data, the list of movie data is cleared.

<h3>Limitations</h3>

   - The bot assumes that the provided OMDb API key and Telegram bot token are valid and active.
   
   - The bot does not handle errors related to network connectivity, API failures, or invalid commands. Error handling and robustness improvements can be implemented based on specific requirements.
