import telebot
import requests
from command import a
from  bs4 import BeautifulSoup as bs
import random
from telebot import types
from passw import gen_random_pass, pah_def
import time
import wikipedia

wikipedia.set_lang('ru')
bot = telebot.TeleBot("")
echo = 'off' 
ben = 0


@bot.message_handler(content_types=['voice'])
def voice(message):
    bot.send_message(message.chat.id, 'У тебя такой крутой голос!')

@bot.message_handler(commands=['random_number'])
def random_num(message):
    if echo == 'on':
        bot.send_message(message.chat.id, message.text)
    try:
        from_ = message.text.split()[1]
        to = message.text.split()[2]
        bot.send_message(message.chat.id, f"После совета со свездами выпало: {random.randint(int(from_), int(to))}")
    except Exception as e:
        bot.send_message(message.chat.id, 'Ты что то делаешь не так, проверь свой iq')

# @bot.message_handler(commands=['weather'])
# def weather1(message):
#     if echo == 'on':
#         bot.send_message(message.chat.id, message.text)
#     bot.send_message(message.chat.id, 'Введи название города в формате Город, Страна\nПример:Moscow, RU')
#     bot.register_next_step_handler(message, get_weather)

# def get_weather(message):
#     try:
#         city = message.text
#         weath = current_weather(city=city)['list'][0]['main']
#         ans = f"Температура: {round(weath['temp'], 1)}\nОщущается как:{round(weath['feels_like'], 1)}"
#         bot.send_message(message.chat.id, ans)
#     except Exception as e:
#         bot.send_message(message.chat.id, "Посмотри как пишется город! И введи его заново!")
#         bot.register_next_step_handler(message, get_weather)

@bot.message_handler(commands=['start'])
def hello(message):
    if echo == 'on':
        bot.send_message(message.chat.id, message.text)
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name} {message.from_user.last_name}\n Я умею следущее:")
    bot.send_message(message.chat.id, a)

@bot.message_handler(commands=['wiki'])
def wiki1(message):
    if echo == 'on':
        bot.send_message(message.chat.id, message.text)
    bot.send_message(message.chat.id, 'Пришли то что ты хочешь узнать')
    bot.register_next_step_handler(message, wiki_searcher)

def wiki_searcher(message):
    bot.send_message(message.chat.id, 'Гуглю')
    try:
        page = wikipedia.page(message.text)
        ans = f"{page.original_title}\n{page.summary[:2000]}\n{page.url}"
        bot.send_message(message.chat.id, ans, parse_mode='html')
    except Exception as e:
        bot.send_message(message.chat.id, 'Похоже про это еще не написали')

@bot.message_handler(commands=['ben_on'])
def ben(message):
    global ben
    if echo == 'on':
        bot.send_message(message.chat.id, message.text)
    bot.send_message(message.chat.id, 'Бен взял трубку')
    ben = 1
    #bot.register_next_step_handler(message, ben_answer)

@bot.message_handler(commands=['ben_off'])
def ben(message):
    global ben
    if echo == 'on':
        bot.send_message(message.chat.id, message.text)
    if ben == 0:
        bot.send_message(message.chat.id, 'Режим Бэна не был включен')
    else:
        bot.send_message(message.chat.id, 'Бен положил трубку')
        ben = 0
    #bot.register_next_step_handler(message, ben_answer)

def ben_answer(message):
    answers = ['да', 'нет', 'охохоххо', 'Брэу']
    bot.send_message(message.chat.id, random.choice(answers))

@bot.message_handler(commands=['who_win'])
def who_win_1(message):
    if echo == 'on':
        bot.send_message(message.chat.id, message.text)
    bot.send_message(message.chat.id, 'Пришли мне через пробел тех кто сражается(не менее двух иначе с кем будет драться твой боец?)')
    bot.register_next_step_handler(message, who_win_2)

def who_win_2(message):
    battlers = str(message.text).split()
    if len(battlers) == 1:
        bot.send_message(message.chat.id, 'Молодец, твоего бойца обсмеяли')
    if len(battlers) == 0:
        bot.send_message(message.chat.id, 'На поле тишина')
    if len(battlers) >= 2:
        bot.send_message(message.chat.id, 'Бойцы выходят')
        time.sleep(2)
        bot.send_message(message.chat.id, 'Идет ожесточенная битва...')
        time.sleep(random.randint(1, 4))
        bot.send_message(message.chat.id, f'{random.choice(battlers).capitalize()} Побеждает!!!')

@bot.message_handler(commands=['help'])
def bot_send_help(message):
    if echo == 'on':
        bot.send_message(message.chat.id, message.text)
    bot.send_message(message.chat.id, a)
  
@bot.message_handler(commands=['random_funny_story'])
def random_story(message):
    if echo == 'on':
        bot.send_message(message.chat.id, message.text)
    a = f"https://www.anekdot.ru/id/{random.randint(13000, 130850)}/"
    print(a)
    req = requests.get(a)
    html = bs(req.content, 'html.parser')
    ans = str(html.find(class_='text')).replace('<br/>', ' ').replace('<div class="text">', '').replace('</div>', '').replace('Владимир', '')
    bot.send_message(message.chat.id, ans)

@bot.message_handler(commands=['gen_password'])
def gen_pass(message):
    if echo == 'on':
        bot.send_message(message.chat.id, message.text)
    sett = str(message.text).split()
    if len(sett) == 1:
        lenght = 8
        lett = 1
        spec = 1
        num = 1
        bot.send_message(message.chat.id, gen_random_pass(lenght=lenght, lett=lett, num=num, spec=spec))
    elif len(sett) > 1:
        try:
            lenght = int(sett[1])
            lett = int(sett[2])
            num = int(sett[3])
            spec = int(sett[4])
            z = 1
        except Exception as e:
            z = 2
    if z != 1:
        bot.send_message(message.chat.id, 'Ты что то делаешь не так!')
    else:
        if pah_def(lenght, lett, num, spec):
            bot.send_message(message.chat.id, 'Сработала защита!')
        else:
            bot.send_message(message.chat.id, gen_random_pass(lenght, lett, num, spec))
        

@bot.message_handler(commands=['hide_markup'])
def hide_markup(message):
    if echo == 'on':
        bot.send_message(message.chat.id, message.text)
    bot.send_message(message.chat.id, 'Markup is hiden', reply_markup=types.ReplyKeyboardRemove())



@bot.message_handler(commands=['get_his_id'])
def get_his_id(message):
    bot.send_message(message.chat.id, 'Перешли мне сообщение и я скажу Id откуда оно пришло')
    bot.register_next_step_handler(message, get_id)

def get_id(message):
    bot.send_message(message.chat.id, message.forward_from.id)

@bot.message_handler(commands=['get_chat_id'])
def chat_id(message):
    bot.send_message(message.chat.id, message.chat.id)

@bot.message_handler(commands=['get_sticker'])
def send_list_stickers(message):
    if echo == 'on':
        bot.send_message(message.chat.id, message.text)
    markup = types.InlineKeyboardMarkup(row_width=3)
    item1 = types.InlineKeyboardButton('Влад', callback_data='vlad')
    item2 = types.InlineKeyboardButton('Да', callback_data='yes')
    item3 = types.InlineKeyboardButton('Че?', callback_data='what')
    item4 = types.InlineKeyboardButton('К телефону', callback_data='phone_call')
    item5 = types.InlineKeyboardButton('Вранье это все', callback_data='lay')
    item6 = types.InlineKeyboardButton('шалю', callback_data='sex')
    item7 = types.InlineKeyboardButton('Молоко?', callback_data='cum')
    item8 = types.InlineKeyboardButton('Секрет', callback_data='secret')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8)
    bot.send_message(message.chat.id, 'Выбери стикер', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def send_a_sticker(call):
    try:
        if call.message:
            if call.data == 'vlad':
                bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAPDYjtcyMsZ4KZkt4TdCULBc6mBUFkAAlgAA11SVSCNrRwjf7kNNSME')
            elif call.data == 'yes':
                bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAO1YjtcMTkXsLJrhrpcvMOgRsrQlswAAiUAAxd7bRfgcfzTd-QR7yME')
            elif call.data == 'what':
                bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAO3YjtcQZsR6t9diQcECGVoA4EBPlAAAgQQAAL8WWBKjsjMfvfkY-YjBA')
            elif call.data == 'phone_call':
                bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAO5YjtcSDOowOmAunqoh6PgPCCVREUAAjwAAxd7bRfFyndUgPtowCME')
            elif call.data == 'lay':
                bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAO7YjtcUukQokpjcXlWTATQ7-tM4iQAAgQAA3ScqRaw-leiwDI4fiME')
            elif call.data == 'sex':
                bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAO9Yjtcgno8kJusdl8uOHBtyGOuv6UAAhcAA3ScqRa-xvN71gkDkSME')
            elif call.data == 'cum':
                bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAPBYjtcrCWmDe3UGa--NOsVcXkwX70AAqQLAAKwGKlLA-3K_VQCHHojBA')
            elif call.data == 'secret':
                bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAO_YjtcnnCcTAX12rPw3a63OvbhsngAAvoNAAK_soBJonhS--JrBqwjBA')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выбери стикер', reply_markup=None)
    except Exception as e:
        print(e)

@bot.message_handler(commands=['get_my_id'])
def get_id_user(message):
    bot.send_message(message.chat.id, message.from_user.id)


@bot.message_handler(commands=['news'])
def news_prepare(message):
    bot.send_message(message.chat.id, 'work is started')



# @bot.message_handler(commands=['random_cat'])
# def random_cat(message):
#     if echo == 'on':
#         bot.send_message(message.chat.id, message.text)
#     p = requests.get("https://thiscatdoesnotexist.com/")
#     pic = p.content
#     bot.send_photo(message.chat.id, pic)

# @bot.message_handler(commands=['random_horse'])
# def random_horse(message):
#     if echo == 'on':
#         bot.send_message(message.chat.id, message.text)
#     p = requests.get("https://thishorsedoesnotexist.com/")
#     pic = p.content
#     bot.send_photo(message.chat.id, pic)

@bot.message_handler(commands=['random_man'])
def random_man(message):
    if echo == 'on':
        bot.send_message(message.chat.id, message.text)
    p = requests.get("https://thispersondoesnotexist.com")
    pic = p.content
    bot.send_photo(message.chat.id, pic)

@bot.message_handler(commands=['echo_on'])
def echo_on(message):
    global echo
    echo = 'on'
    bot.reply_to(message, message.text)

@bot.message_handler(commands=['echo_off'])
def echo_off(message):
    global echo
    echo = 'off'
    bot.reply_to(message, "режим эхо выключен")

@bot.message_handler(content_types=['sticker'])
def send_id(message):
    bot.send_message(message.chat.id, f"{message.sticker.file_id} - id стикера", reply_to_message_id=message.message_id)
    
@bot.message_handler(content_types=['text'])
def send_smth(message):
    if echo == 'on':
        bot.send_message(message.chat.id, message.text)
    if ben == 1:
        ben_answer(message)
    if '/' in message.text:
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIDVmI8vj9gAgv2BmdC4GVjmGf33mIbAAJkAAMNSyERa9zWoQpUSrAjBA')
        bot.send_message(message.chat.id, "Я не понял какую команду ты от меня хочешь...\nВызови команду /help")
    else:
        bot.send_message(message.chat.id, "Мне пофиг")
    print(f"id откуда: {message.chat.id}\nимя: {message.from_user.first_name}\nчто написал: {message.text}")




bot.infinity_polling()