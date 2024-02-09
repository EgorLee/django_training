import requests
from telebot.models import TeleSettings


def sendTelegram(tg_name, tg_phone):
		tele_object = TeleSettings.objects.first()
		token = tele_object.tg_token
		chat_id = tele_object.tg_chat
		text = f"Клиент: {tg_name}. Телефон: {tg_phone}"
		api = 'https://api.telegram.org/bot'
		method = api + token + '/sendMessage'
		print(text)


		try:
			req = requests.post(method, data={
				'chat_id': chat_id,
				'text': text
				})
		except:
			pass

		finally:
			if req.status_code != 200:
				print('Ошибка отправки!')
			elif req.status_code == 500:
				print('Ошибка 500')
			else:
				print('Всё Ок сообщение отправлено!')
