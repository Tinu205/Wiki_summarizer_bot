import telebot
import os
import wikipedia

MAX_CHAR_LIMIT = 4065

###Class to use wiki module
class Wikicontext:
    def __init__(self,topic):
        self.topic = topic
    def summary(self):
        try:
            content = wikipedia.summary(self.topic)
        except (IndexError , wikipedia.PageError):
            return f"Page not found"
        
        except wikipedia.exceptions.DisambiguationError as e:
            topic =[]
            for option in e.options:
                if ("All pages") not in option:
                    topic.append(option)
            topic = str(topic)
            return f'Can\'t find the topic, similar pages -> {topic.replace("[","").replace("]","").strip()}'        
        else:
            return content
        
##function to write content in data.txt
def write_data(data):
    with open("data.txt","a") as file:
        file.write(data)
        file.close()

#Get the bot token
bot_tok = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(bot_tok)

## Bot reply
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi type /help to get help")
    write_data(f"{message.from_user.first_name} -> {message.text} \n")
    write_data(f"Bot -> Welcome message \n\n")

@bot.message_handler(commands = ["help"])
def give_help(message):
    bot.reply_to(message,"Type /get <topic> you need to research on")
    write_data(f"{message.from_user.first_name} -> {message.text} \n")
    write_data(f"Bot -> Type /get <topic> you need to research on \n\n")

#The requestior
@bot.message_handler(commands = ['get'],content_types=['text'])
def send_request(message):
    topic = Wikicontext(message.text.replace("/get","").strip())
    content = topic.summary()
    if(len(content) > MAX_CHAR_LIMIT):
        arr = content.split()
        for chung in arr:
            bot.reply_to(message,chung)
    else:
        bot.reply_to(message,content)
        write_data(f"{message.from_user.first_name} -> {message.text} \n")
    write_data(f"Bot -> {content} \n\n")


bot.infinity_polling()