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

from requests.exceptions import ReadTimeout
from requests.exceptions import ConnectionError


token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)
vip=[441399484, 55888804]
games={}
skills=[]

client1=os.environ['database']
client=MongoClient(client1)
db=client.farmer
users=db.users


bot.message_handler(commands=['start'])
def start(m):
   if users.find_one({'id':m.from_user.id})==None:


  
if True:
 try:
   print('7777')
   bot.polling(none_stop=True,timeout=600)
 except (requests.ReadTimeout):
        print('!!! READTIME OUT !!!')           
        bot.stop_polling()
        time.sleep(1)
        check = True
        while check==True:
          try:
            bot.polling(none_stop=True,timeout=1)
            print('checkkk')
            check = False
          except (requests.exceptions.ConnectionError):
            time.sleep(1)
   
   
   
def createuser(id):
   return{'id':id,
          'coal':0,
          'iron':0,
          'gold':0,
          'diamond':0,
          'wood':0,
          'rock':0,
          'money':0,
          'sand':0,
          'salt':0,
          'ruby':0,
          'shugar':0,
          'mushroom':0,
          'meat':0,
          'fish':0,
          'egg':0,
          'water':0,
          'iridium':0,
          'hunger':100,
          'maxhunger':100,
          'buildings':[],
          'farm':None,
          'animals':[],
          'exp':0,
          'level':1
          
          
          

   
#if __name__ == '__main__':
 # bot.polling(none_stop=True)

#while True:
#    try:
  #      bot.polling()
 #   except:
  #      pass
#    time.sleep(1)
       
