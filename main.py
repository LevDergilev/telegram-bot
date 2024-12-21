import telebot
from bot_logic import gen_pass, gen_emodji, flip_coin

# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("TOKEN ID")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
        bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

    
@bot.message_handler(commands=['hello'])
def send_hello(message):
        bot.reply_to(message, "Привет! Как дела?")

    
@bot.message_handler(commands=['bye'])
def send_bye(message):
        bot.reply_to(message, "Пока! Удачи!")


@bot.message_handler(commands=['pass'])
def get_pass(message):
        bot.reply_to(message, gen_pass(10))       

@bot.message_handler(commands=['smile'])
def get_smile(message):
        smile = gen_emodji()
        bot.reply_to(message, {smile})

@bot.message_handler(commands=['monetka'])
def get_monetka(message):
        monetka = flip_coin()
        bot.reply_to(message, {monetka})

    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
        bot.reply_to(message, message.text)
    
bot.polling()
