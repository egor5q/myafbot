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


@bot.message_handler(commands=['start'])
def start(m):
   if users.find_one({'id':m.from_user.id})==None and m.chat.id==m.from_user.id:
      users.insert_one(createuser(m.from_user.id, m.from_user.first_name))
      kb=types.ReplyKeyboardMarkup()
      kb.add(types.KeyboardButton('👷🏻Добыча'))
      bot.send_message(m.chat.id, '''Здраствуй, ты попал в игру "Survival simulator"!
*Предыстория:*
На земле появился вирус, превращающий людей в зомби, передающийся через укус. В скором времени Почти всё
население земли было заражено, и оставшимся в живых ничего не оставалось, кроме переселения на необитаемые острова.
Так как все, кого вы знали, были заражены, вы в одиночку построили плот, взяли минимум необходимых вещей, и отправились в плавание.
Через 3 дня плавания, в 5 часов утра, вы увидели берег какого-то острова. Первым делом, после высадки, вы решили, что нужно построить дом.
Для этого нужно дерево. Чтобы начать добывать его, нажмите кнопку "👷Добыча", а затем - кнопку "🌲Лес".''', parse_mode='markdown', reply_markup=kb)


                       
@bot.message_handler(content_types=['text'])
def text(m):
   if m.from_user.id==m.chat.id:
    x=users.find_one({'id':m.from_user.id})
    if x!=None:
      if x['tutorial']==1:
         if m.text=='👷🏻Добыча':
            kb=types.ReplyKeyboardMarkup()
            kb.add(types.KeyboardButton('🌲Лес'))
            bot.send_message(m.chat.id, 'Куда вы хотите направиться?', reply_markup=kb)
         elif m.text=='🌲Лес' and x['tforest']==0:
            bot.send_message(m.chat.id, 'Вы отправились в лес. Вернётесь через минуту (Минута вашего времени = 30 минут жизни на острове).')
            users.update_one({'id':m.from_user.id}, {'$set':{'tforest':1}})
            t=threading.Timer(60, tforest, args=[m.from_user.id])
            t.start()
         elif m.text=='🔨Постройка':
            kb=types.ReplyKeyboardMarkup()
            kb.add(types.KeyboardButton('⛺️Дом'))
            bot.send_message(m.chat.id, 'Что вы хотите построить?', reply_markup=kb)
         elif m.text=='⛺️Дом' and x['thouse']==0:
            users.update_one({'id':m.from_user.id}, {'$set':{'thouse':1}})
            bot.send_message(m.chat.id, 'Вы отправились строить дом. Вернётесь через 2 минуты.')
            users.update_one({'id':m.from_user.id}, {'$inc':{'wood':-1000}})
            t=threading.Timer(120, thouse, args=[m.from_user.id])
            t.start()
               
            


def tforest(id):
   kb=types.ReplyKeyboardMarkup()
   kb.add(types.KeyboardButton('🔨Постройка'))
   users.update_one({'id':id}, {'$inc':{'wood':1000}})
   bot.send_message(id, 'Прошло пол часа. С помощью топора, который вы взяли с собой в путь, вы добыли 1000 ед. дерева -'+
   ' Этого должно хватить на постройку дома. Чтобы начать постройку, нажмите кнопку "🔨Постройка", и выберите пункт "⛺️Дом".', reply_markup=kb)
 


def thouse(id):
   kb=types.ReplyKeyboardMarkup()
   bot.send_message(id, 'Поздравляю! Вы построили себе дом! Здесь вы сможете спастись от дикой природы и от холода.'+
                    ' Дальше выживать придётся самостоятельно. Но осторожнее: добывая ресурсы, вы можете встретить других игроков, и если'+
                    ' они будут сильнее вас - добычу придётся отдать.', reply_markup=kb)
   users.update_one({'id':id}, {'$set':{'tutorial':0}})
                    
                   
              
         
 
def createuser(id, name):
   return{'id':id,
          'name':name,
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
          'level':1,
          'tutorial':1,
          'tforest':0,
          'thouse':0
         }


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
   
   
        

   
#if __name__ == '__main__':
 # bot.polling(none_stop=True)

#while True:
#    try:
  #      bot.polling()
 #   except:
  #      pass
#    time.sleep(1)
       
