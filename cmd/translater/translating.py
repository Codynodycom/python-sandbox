from translate import Translator

lang = ''
possible = False

def select_translator():
    global lang, possible
    lang = input('Выберите переводчик:\n[0] - русско-агнглийский\n[1] - русско-немецкий\n[2] - англо-русский\n[3] - англо-немецкий\n[4] - немецко-русский\n[5] - немецко-английский\n')
    # проверка
    if lang in '012345':
        for i in '012345':
            #print(i)
            if lang==i: possible= True
    else:
        print('Такого языка нет.')
        select_translator()

def translate_message(mess):
    #print(lang, possible)
    if possible is True and lang=='0':
        tran= Translator(to_lang="en", from_lang="ru") # ru_to_en
    elif possible is True and lang=='1':
        tran= Translator(to_lang="de", from_lang="ru") # ru_to_deu
    elif possible is True and lang=='2':
        tran= Translator(to_lang="ru", from_lang="en") # en_to_rus
    elif possible is True and lang=='3':
        tran= Translator(to_lang="de", from_lang="en") # en_to_deu
    elif possible is True and lang=='4':
        tran= Translator(to_lang="ru", from_lang="de") # deu_to_ru
    elif possible is True and lang=='5':
        tran= Translator(to_lang="en", from_lang="de") # deu_to_en

    ans = tran.translate(mess)
    return ans


select_translator()
inp_text = input('Введите текст для перевода:\n')
translate_text = translate_message(inp_text)
print('Перевод:',translate_text)
