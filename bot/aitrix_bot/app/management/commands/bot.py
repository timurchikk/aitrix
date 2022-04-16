from django.core.management.base import BaseCommand

import telebot

from telebot import types

TOKEN = '5146117726:AAHenGNCtJSKOCAqJoswtqSdqpHOESMhL4s'

from app.models import *

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    global chat_id
    chat_id = message.chat.id
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    username = message.chat.username
    user = User(
        user_id=chat_id,
        first_name=first_name,
        last_name=last_name,
        username=username
    )
    user.save()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    tests = types.KeyboardButton('Тесты', callback_data='test')
    markup.add(tests)
    bot.send_message(message.chat.id, f"Hi! {first_name}".format(
        message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler()
def test(message):
    chat_id = message.chat.id
    user = User.objects.get(user_id=chat_id).id
    category = Category.objects.get(user=user).title
    if message.chat.type == 'private':
        bot.send_message(message.chat.id, "Ok. Lets start")
        markup = types.InlineKeyboardMarkup(row_width=1)
        button = types.InlineKeyboardButton(text=f"{category}", callback_data='start')
        markup.add(button)


@bot.callback_query_handler(func=lambda call:True)
def category(call):
    user = User.objects.get(user_id=chat_id)
    user_id = User.objects.get(user_id=chat_id).id
    question = Test.objects.get(user=user_id).question
    try:
        if call.data == "start":
            bot.send_message(call.message.chat.id, f"{question}")
            answer = call.text
            answers = Answers(
                user=user,
                test=question,
                answer=answer
            )
            answers.save()

    except Exception as e:
        print(e)


class Command(BaseCommand):
    help = 'Telegram-Bot'

    def handle(self, *args, **options):
        print('Бот запущен!')
        bot.polling(none_stop=True)