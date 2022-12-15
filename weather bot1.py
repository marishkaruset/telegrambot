import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config
from telebot import types 


bot = telebot.TeleBot("5227063280:AAGmhszDSHRRyXaSeZYp9nLUWhCnZBTBgtw")

@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id, 'Добро пожаловать, ' + str(message.from_user.first_name) + ',\nЧтобы узнать прогноз одежды напишите в чат название города')

@bot.message_handler(content_types=['text'])
def test(message):
	try:
		place = message.text

		config_dict = get_default_config()
		config_dict['language'] = 'ru'

		owm = OWM('421e91f66d1a744c0578eececec50f63', config_dict)
		mgr = owm.weather_manager()
		observation = mgr.weather_at_place(place)
		w = observation.weather

		t = w.temperature("celsius")
		t1 = t['temp']
		t2 = t['feels_like']

		wi = w.wind()['speed']
		humi = w.humidity
		dt = w.detailed_status

		
		if t2 <= -15 and t2 >= -40: 
			bot.send_message(message.chat.id,  "В городе " + str(place) + " температура " + str(t1) + " °C" + "\n" + 
				"🌡Ощущается как " + str(t2) + " °C" + "\n" +
				"💨Скорость ветра " + str(wi) + " м/с" + "\n" + 
				"💧Влажность " + str(humi) + " %" + "\n" + 
				"⛅️" + str(dt) + "\n" +
				'Вам стоит надеть:' + "\n" +
				'Варежки, шарф, зимнюю куртку/пальто/шубу, шапку, тёплые носки, обувь на толстой подошве,теплый свитер, под брюки надеть термобелье.')
				
		elif t2 <= -9 and t2 >= -14:
			bot.send_message(message.chat.id, "В городе " + str(place) + " температура " + str(t1) + " °C" + "\n" + 
				"🌡Ощущается как " + str(t2) + " °C" + "\n" +
				"💨Скорость ветра " + str(wi) + " м/с" + "\n" + 
				"💧Влажность " + str(humi) + " %" + "\n" + 
				"⛅️" + str(dt) + "\n" +
				'Вам стоит надеть:' + "\n" +
				'Перчатки, шарф, зимнюю куртку/пальто, теплый свитер, джинсы, шапку, обувь на толстой подошве.')

		elif t2 <= -5 and t2 >= -8:
			bot.send_message(message.chat.id, "В городе " + str(place) + " температура " + str(t1) + " °C" + "\n" + 
				"🌡Ощущается как " + str(t2) + " °C" + "\n" +
				"💨Скорость ветра " + str(wi) + " м/с" + "\n" + 
				"💧Влажность " + str(humi) + " %" + "\n" + 
				"⛅️" + str(dt) + "\n" +
				'Вам стоит надеть:' + "\n" +
				'Трикотажное (шерстяное) платье/теплую рубашку с теплыми брюками; трикотажная (шерстяная) кофта; колготки; зимняя куртка/пальто; шапка; сапоги; перчатки.')
		
		elif t2 <= -1 and t2 >= -4:
			bot.send_message(message.chat.id,"В городе " + str(place) + " температура " + str(t1) + " °C" + "\n" + 
				"🌡Ощущается как " + str(t2) + " °C" + "\n" +
				"💨Скорость ветра " + str(wi) + " м/с" + "\n" + 
				"💧Влажность " + str(humi) + " %" + "\n" + 
				"⛅️" + str(dt) + "\n" +
				'Вам стоит надеть:' + "\n" +
				'Теплое платье/теплую водолазку с брюками; куртку/пальто; сапоги/теплые кроссовки; шапку; перчатки.')


		elif t2 <=7 and t2 >= 0:
			bot.send_message(message.chat.id, "В городе " + str(place) + " температура " + str(t1) + " °C" + "\n" + 
				"🌡Ощущается как " + str(t2) + " °C" + "\n" +
				"💨Скорость ветра " + str(wi) + " м/с" + "\n" + 
				"💧Влажность " + str(humi) + " %" + "\n" + 
				"⛅️" + str(dt) + "\n" +
				'Вам стоит надеть:' + "\n" +
				'Теплое платье/теплую водолазку с брюками; куртку/пальто; сапоги/ кроссовки.' ) 

		elif t2 <= 12 and t2 >= 8:
			bot.send_message(message.chat.id, "В городе " + str(place) + " температура " + str(t1) + " °C" + "\n" + 
				"🌡Ощущается как " + str(t2) + " °C" + "\n" +
				"💨Скорость ветра " + str(wi) + " м/с" + "\n" + 
				"💧Влажность " + str(humi) + " %" + "\n" + 
				"⛅️" + str(dt) + "\n" +
				'Вам стоит надеть:' + "\n" +
				'Трикотажное или шерстяное платье/рубашку; теплую кофту; колготы; теплые штаны; обувь - кроссовки/ботинки. ')
		
		elif t2 <= 16 and t2 >= 13:
			bot.send_message(message.chat.id, "В городе " + str(place) + " температура " + str(t1) + " °C" + "\n" + 
				"🌡Ощущается как " + str(t2) + " °C" + "\n" +
				"💨Скорость ветра " + str(wi) + " м/с" + "\n" + 
				"💧Влажность " + str(humi) + " %" + "\n" + 
				"⛅️" + str(dt) + "\n" +
				'Вам стоит надеть:' + "\n" +
				'Трикотажное или шерстяное платье/рубашка; теплую кофту/легкую куртку; колготы; теплые штаны; обувь - кроссовки/ботинки.')

		elif t2 <= 30 and t2 >= 17:
			bot.send_message(message.chat.id,  "В городе " + str(place) + " температура " + str(t1) + " °C" + "\n" + 
				"🌡Ощущается как " + str(t2) + " °C" + "\n" +
				"💨Скорость ветра " + str(wi) + " м/с" + "\n" + 
				"💧Влажность " + str(humi) + " %" + "\n" + 
				"⛅️" + str(dt) + "\n" +
				'Рекомендуемая ткань: хлопок, лён; крой - свободный; низ - шорты/юбка; платье, блузка/ футболка/рубашка с коротким рукавом или без; головной убор с полями (шляпа) или козырьком (кепка); не забыть про солнцезащитный крем.')

		else:
			bot.send_message(message.chat.id, 'Упс, проблемка, не можем определить погоду, об ошибке напишите @rusetskaya')

	except:
		bot.send_message(message.chat.id,"Такой город не найден!")
		print(str(message.text),"- не найден")

bot.polling(none_stop=True, interval=0)