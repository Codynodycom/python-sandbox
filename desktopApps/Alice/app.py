
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

def get_time():
	time = datetime.datetime.now()
	return f"Сейчас {time.hour} часов и {time.minute} минуты"


def say(phrase):
    print(f'я говорю: {phrase}')

	# скорость
    rate = speak_engine.getProperty('rate')
    speak_engine.setProperty('rate', rate + 10)

    speak_engine.say(phrase)
    speak_engine.runAndWait()
    speak_engine.stop()

def command():
	r = sr.Recognizer()

	# Начинаем прослушивать микрофон и записываем данные в source
	with sr.Microphone() as source:
		print("Говорите")
		# Устанавливаем паузу, чтобы прослушивание
		# началось лишь по прошествию 1 секунды
		r.pause_threshold = 1

		# удаление посторонних шумов из аудио дорожки
		r.adjust_for_ambient_noise(source, duration=1)
		# Полученные данные записываем в переменную audio
		# mp3 звук
		audio = r.listen(source)

	try:
		zadanie = r.recognize_google(audio, language="ru-RU").lower()
		print("Вы сказали: " + zadanie)

	# Если не смогли распознать текст, то будет вызвана эта ошибка
	except sr.UnknownValueError:
		say("Я вас не поняла")
		zadanie = command()

	# В конце функции возвращаем текст задания
	# или же повторный вызов функции
	return zadanie

# Проверяем слова
def checkWords(zadanie):

	if "коробочка который час" in zadanie:
		say(get_time())

	elif "коробочка ты читаешь мангу" in zadanie:
		say("ты ещё спрашиваешь! канееешна! Смотри какую начала на прошлой неделе")
		webbrowser.open("https://www.ozon.ru/product/ataka-na-titanov-kniga-1-135331418/?sh=W6j7IwAAAA")

	elif "коробочка о чём думаешь" in zadanie:
		say("я думаю, что на марсе определённо можно жить")

	elif "коробочка включи свою любимую песню" in zadanie:
		say("Женя, как будто ты не знаешь. Я обожаю моргенштерна")
		webbrowser.open("https://music.yandex.ru/album/16164165/track/75630144")

	else:
		say("Ты ещё не научил меня отвечать на такие вопросы. Когда научишь, тогда отвечу")


speak_engine = pyttsx3.init()
say("Привет. Давно не виделись. Спроси меня о чем нибудь")
while True:
	checkWords(command())



