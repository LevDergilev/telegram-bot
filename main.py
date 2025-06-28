import telebot
from bot_logic import gen_pass, gen_emodji, flip_coin, get_class
from tokenid import token
import random
import os

# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    # Проверяем, есть ли фотографии
    if not message.photo:
        return bot.send_photo(message.chat.id, "Вы не загрузили картинку")
    # Получаем файл и сохраняем его
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]

    # Загружаем файл и сохраняем
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
          new_file.write(downloaded_file)
    result = get_class(model_path="keras_model.h5", labels_path="labels.txt", image_path=file_name)
    bot.send_message(message.chat.id, result)
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
        bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь! Для вывода списка команд напиши /help Отправь фото ядовитого гриба чтобы узнать его название ")

   
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


@bot.message_handler(commands=["poll"])
def create_poll(message):
    bot.send_message(message.chat.id, "English Article Test")
    answer_options = ["a", "an", "the", "-"]

    bot.send_poll(
        chat_id=message.chat.id,
        question="We are going to '' park.",
        options=answer_options,
        type="quiz",
        correct_option_id=2,
        is_anonymous=False,
    )


@bot.message_handler(commands=['mem'])
def send_mem(message):
    img_name = random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['help'])
def send_help(message):
        bot.reply_to(message, "Команды моего бота:\n1./start - запуск бота\n2./hello - приветсвие от бота\n3./bye - прощание от бота\n4./pass - генерация пароля\n5./smile - случайный смайлик\n6./monetka - Орел или Решка\n7./poll - голосование с выбором ответов\n8./mem - случайная мемная картинка\n9./help - команды используемые в боте")

@bot.poll_answer_handler()
def handle_poll(poll):
    # This handler can be used to log User answers and to send next poll
    pass


bot.infinity_polling()

    
bot.polling()
