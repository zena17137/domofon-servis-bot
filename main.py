from config import token, mennanger_id_zena
import telebot
from telebot import types


bot = telebot.TeleBot(token)

mennanger_id = mennanger_id_zena

cid = 0


def sendMess(message):
	bot.send_message(cid, message)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	global cid
	cid = message.chat.id

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton('Аудіо')
	item2 = types.KeyboardButton('Відео')

	sendMess('Вас вітає доммофонна компанія \'Домофон Сервіс\'.')
	sendMess('Ми можемо встановити вам в квартиру аудіо або відео трубку. Є варіанти аудіо та відео трубок напишіть які ви хочете подивитись.')


	markup.add(item1, item2)


@bot.message_handler(content_types='text')
def sdfsdf(message):
	if message.text.lower() == 'аудіо':
		ykp7 = open('img/укп7.jpg', 'rb')
		ykp12 = open('img/укп12.jpg', 'rb')
		ykp12m = open('img/укп12м.jpg', 'rb')
		sendMess('Є ось такі варіанти аудіо трубок:')
		sendMess('УКП7 - 250грн: ')
		bot.send_photo(cid, ykp7)
		sendMess('УКП12 - 350грн: ')
		bot.send_photo(cid, ykp12)
		sendMess('УКП12м - 450грн: ')
		bot.send_photo(cid, ykp12m)
		sendMess('Ціни на момент замовлення, можуть відрізнятися від заявлених, в зв\'язку з нестабільною ситуацією в країні.')
		sendMess('Встановлення аудіо трубки складається з 2-ох компонентів:')
		sendMess('1) Вартість допідключення (кожна адреса має різну вартість до підключення, її величина залежить від початкових умов домовленостей з забудовником)')
		sendMess('2) ціна аудіо трубки та її монтаж.')
		sendMess('Для того, щоб оформити заявку на встановлення обраної аудіо або відео трубки, напишіть свою адресу, контактний телефон та модель апарату. Якщо ви захочете змінити модель апарату будь-ласка повідомте своє рішення телефоним дзвінком консультанту 0676754310 - Євген.')
		sendMess('Введіть вашу адресу та номер телефону та незабаром з вами звяжеться меннанджер з допідключення.')
		sendMess('Хочете подивитись відео трубки? Нажміть /start та виберіть Відео')
	elif message.text.lower() == 'відео':
		sendMess('Є ось такі варіанти відео трубок:')
		sq04 = open('img/SL-04.jpg', 'rb')
		sq04m = open('img/SL-04M.jpg', 'rb')
		sl07iphd = open('img/SL-07IPHD.jpg', 'rb')
		sonik_7_cloud = open('img/Sonik_7_cloud.png', 'rb')
		sonik_10 = open('img/Sonik_10.png', 'rb')
		sm_07m = open('img/SM_07M.png', 'rb')
		sendMess('Ціни на відео трубки разом з монтажем')
		sendMess('Slinex SQ-04 - від 2000грн(в наявності немає).')
		bot.send_photo(cid, sq04)
		sendMess('Slinex SQ-04M - від 4000грн.')
		bot.send_photo(cid, sq04m)
		sendMess('Slinex SL-07IPHD - від 8000грн.')
		bot.send_photo(cid, sl07iphd)
		sendMess('Slinex Sonik 7 - від 8000грн.')
		bot.send_photo(cid, sonik_7_cloud)
		sendMess('Slinex Sonik 10 - від 1160грн.')
		bot.send_photo(cid, sonik_10)
		sendMess('Slinex SM-07M - від 5000грн.')
		bot.send_photo(cid, sm_07m)
		sendMess('Ціни на момент замовлення, можуть відрізнятися від заявлених, в зв\'язку з нестабільною ситуацією в країні.')
		sendMess('1) Вартість допідключення (кожна адреса має різну вартість до підключення, її величина залежить від початкових умов домовленостей з забудовником)')
		sendMess('2) ціна аудіо трубки та її монтаж.')
		sendMess('Для того, щоб оформити заявку на встановлення обраної аудіо або відео трубки, напишіть свою адресу, контактний телефон та модель апарату. Якщо ви захочете змінити модель апарату будь-ласка повідомте своє рішення телефоним дзвінком консультанту 0676754310 - Євген.')
		sendMess('Введіть вашу адресу та номер телефону та незабаром з вами звяжеться меннанджер з допідключення.')
		sendMess('Хочете подивитись аудіо трубки? Нажміть /start та виберіть Аудіо')
	else:
		address = message.text
		bot.send_message(mennanger_id_zena, 'Ім\'я: ' + message.from_user.first_name + '; Юзернейм: ' + message.from_user.username + '; Адресса: ' + address)


if __name__ == '__main__':
	bot.polling(none_stop=True)