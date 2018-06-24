# -*- coding: utf-8 -*-
import os
import telebot
import time
import telebot
import random
import info
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
from telethon import TelegramClient
from requests.exceptions import ReadTimeout
from requests.exceptions import ConnectionError
from telethon import events

api_id=os.environ['api_id']
api_hash=os.environ['api_hash']


bot = TelegramClient('session_name', api_id, api_hash)

phone_number = '+79268508530'
#bot.send_code_request(phone_number)
#myself = bot.sign_in(phone_number, input('Enter code: '))


#assert bot.connect()
#if not bot.is_user_authorized():
#    bot.send_code_request(phone_number)
#    me = bot.sign_in(phone_number, input('Enter code: '))


bot.start()

#bot.updates.workers = 1

#@bot.on(events.NewMessage(incoming=True, pattern='/go'))
#def handler(event):
#    event.reply('Hello!')






#if True:
# try:
#   print('7777')
#   bot.polling(none_stop=True,timeout=600)
# except (requests.ReadTimeout):
#        print('!!! READTIME OUT !!!')           
#        bot.stop_polling()
#        time.sleep(1)
#        check = True
#        while check==True:
#          try:
#            bot.polling(none_stop=True,timeout=1)
#            print('checkkk')
#            check = False
#          except (requests.exceptions.ConnectionError):
#            time.sleep(1)
   
   
        

   
#if __name__ == '__main__':
 # bot.polling(none_stop=True)

#while True:
#    try:
  #      bot.polling()
 #   except:
  #      pass
#    time.sleep(1)
       
