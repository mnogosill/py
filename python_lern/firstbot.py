''''#!/usr/bin/env python

import random

import telebot
from telebot.types import Message



token='991952168:AAFDCJ3bnrQnf5RcDZAfaK0r6fogu_SQ0_E'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    bot.reply_to(message, 'This is no answer')


@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo_digits(message: Message):
    bot.reply_to(message, str(random.random()))




bot.polling(timeout=60)

'''

import apiai
import json




def send_message(message): #-------------- begin func
    request = apiai.ApiAI('b9f933e583d64505854404ec5c02f829').text_request() #-------подключение с отправкой запроса
    request.lang = 'ru' #-----проверка языка
    request.session_id = 'session_1'   #------- групировка от одного пользователя по id сессии
    request.query = message #-------- запрос с сообщением от пользователя
    response = json.loads(request.getresponse().read().decode('utf-8')) #-------получение овтета/прочтение/конвертировка в utf-8
    print(response['result']['fulfillment']['speech'])#-------- печать ответа
    return response(['result'['action']])



print('input message') #-----призыв к действию/уточнение
message = input() #----- сообщение
action = None
while True:
    action = send_message(message) #----- проверка чтобы action был не None
    if action == 'smalltalk.greetings.bye':
        break
    message = input() #------  повторный ввод

send_message(input()) #---------вызов функции


