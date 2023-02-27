import telebot
import misc
from datetime import datetime
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

providers = [
    misc.ElitTrade, misc.Armia5, misc.Arzu, 
    misc.OOONDN, misc.TruFru, misc.OMKIrk,
    misc.SyrovarIrk, misc.MorskoiIP, misc.MamaFerma, misc.Beloreche]
not_found = []

bot = telebot.TeleBot(misc.tgtoken)


def check_not_found(request: list) -> list:
    global not_found
    result = []
    print(not_found)
    for position in request:
        if position not in not_found:
            result.append(position)
    
    return result


def reqestProcessing(chatid, request: list, provider):
    rawApplication = ''
    global not_found
    for position in request:
        if fuzz.token_set_ratio(position, provider) > 60:
            rawApplication = rawApplication + '\n' + position
            not_found.append(position)
    if len(rawApplication) > 1:
        if provider == misc.ElitTrade:
            bot.send_message(
                chatid, 'Elite trade +79143033666 Любовь \nДоброго времени суток, заявка на - \n' + rawApplication)
        if provider == misc.Armia5:
            bot.send_message(
                chatid, '5 Армия +79246020213 Анна\nДоброго времени суток, заявка на  - \n' + rawApplication)
        if provider == misc.Arzu:
            bot.send_message(
                chatid, 'Арзу +79149016763 +79245455893 \nДоброго времени суток, заявка на  - \n' + rawApplication)
        if provider == misc.OOONDN:
            bot.send_message(
                chatid, 'ООО НДН +79148785017 Максим \nДоброго времени суток, заявка на - \n' + rawApplication)
        if provider == misc.TruFru:
            bot.send_message(
                chatid, 'Труфру Группа What`s App\nДоброго времени суток, заявка на - \n' + rawApplication)
        if provider == misc.OMKIrk:
            bot.send_message(
                chatid, 'ОМК Иркуткск +79500663307 Татьяна\nДоброго времени суток, заявка на - \n' + rawApplication)
        if provider == misc.SyrovarIrk:
            bot.send_message(
                chatid, 'Иркутский сыровар +79246086999 Василина\nДоброго времени суток, заявка на - \n' + rawApplication)
        if provider == misc.MorskoiIP:
            bot.send_message(
                chatid, 'ИП Морской А.Н. +79025781856 А.Н.\nДоброго времени суток, заявка на - \n' + rawApplication)
        if provider == misc.MamaFerma:
            bot.send_message(
                chatid, 'Мама ферма +79025664449 Вадим\nДоброго времени суток, заявка на - \n' + rawApplication)
        if provider == misc.Beloreche:
            bot.send_message(
                chatid, 'Белоречье +79027630361 Адрей \nДоброго времени суток, заявка на - \n' + rawApplication)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, """Позиции, такие как 'шпинат с/м' и 'шпинат свежий' могут дублироваться, придется пока проверять и редактировать вручную. \n
        Если название короткое, по типу 'Рис', мы добавляем туда вес и процент совпадения уменьшается за счет длины строки. С более длинными названиями соответственно таких проблем не возникает\n
        Можно будет писать пока просто Рис в общую заявку, а при пересылании сообщения - добавлять вес вручную  """)


#@bot.message_handler(commands=['time'])
#def now_time(message):
#   now = datetime.now()
#   chatid = message.chat.id
#   if now.hour in timecheck:
#       bot.send_message(chatid, 'Пора чистить гидрофильтр')

@bot.message_handler(content_types=['text'])
def function_name(message):
    chatid = message.chat.id
    raw_Request = message.text
    request = raw_Request.split('\n')

    for provider in providers:
        reqestProcessing(chatid=chatid, request=request, provider=provider)

    invalid_positions = check_not_found(request=request)
    if invalid_positions:
        text = '\n'.join(invalid_positions) + '\n----------------------------\nНе удалось найти ни у одного поставщика'
        print(text)
        bot.send_message(chat_id=chatid, text=text)


bot.infinity_polling()