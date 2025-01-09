import telethon
import logging
import sqlite3
import asyncio
import datetime
import random
from telethon.sync import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.channels import GetMessagesRequest
from telethon.tl.functions.messages import GetHistoryRequest, GetMessagesViewsRequest, ImportChatInviteRequest
from telethon.tl.types import InputPeerChannel

API_ID2 = 21653220
API_HASH2 = '0a5270cde18fed26deef4a2a67916c9d'
session2 = '1ApWapzMBuzB3UkqtfBEFO1tyKtF-tYrS9q4OMC4nGr4WcIfFHxfZzVcbi0mAMQ2XcSAfFOLTGv86ofb5nY_cPq_SPYiWddhSa5YaQEGCZZ_izPfsbGvTSCuVgGghqmOXv_DRpd1KwM63JaZWC8zpaqJtBDRorspPG9mEZuxFEhsemupDikcl_LO7fZHleXZ_OWd5nKKXDXz1Os89nk0lP7ztk7dfbpyv46t2L98S1cFnZNOa6px2qOQfNiw6VFz7xU7B0uJymY6PA1VXQd48l6_oeWjod54PESIzQge0A39BI2HvKKIQeg_k1VXtx3C8nbuHZVOhFPNITErnpaopJBC7X0nRB3E='


API_ID=23473442
API_HASH='0cd1d983e8b65e8d992b3b756f9a8eb1'
session = '1ApWapzMBu8ainhul7iGgzwlE031N4KAYUlyzH_hzsI2hTRuAADEx8n2OI-Gbpc_TY1MchLNNAgRkEAkob2Hor8YEXtSo8IQCjsvu1AdZQqp-QGcnhUNFcqfa9D4-SZgl3A5i7Db-bafrAqmcSSvEEUZ6vsJuVatsFpJXJFVYk2RHeX9Bu1wBXNhQ4rPsVu4dpx7bkGbXftZDsSjQrmaSE3_rC4p3fbp5h8QrrkBB0K16VrSIts7N_N2MvbM6E9jWrRNAXj3UpZM2PfUblobn4Ewea3f1Kdu27_eMuKHPhc6S8lLxzA9IIgiIZcLCbUi-e4xRSv_5OYZ2FJ-EASuDmV8xJsnZ-b4='
logging.basicConfig(level=logging.INFO)

last = None

connection = sqlite3.connect("farming.db")
cursor = connection.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY,
user_id INT,
time INT,
state1 INT,
state2 INT,
farm_location STR,
hp1 INT,
hp2 INT  
)
""")

def insert_into():
    profile = cursor.execute('SELECT * FROM users WHERE user_id = ?', (1776244625,)).fetchone()
    print(profile)
    if profile == None:
        cursor.execute('INSERT INTO users (user_id, time, state1, state2, farm_location, hp1, hp2) VALUES (?, ?, ?, ?, ?, ?, ?)', (1776244625, None, 0, 0, None, None, None))
        connection.commit()

insert_into()

client = TelegramClient(StringSession(session), API_ID, API_HASH, system_version='4.16.30-vxCUSTOM', device_model='aboba-windows-custom', app_version='1.1.0')
client2 = TelegramClient(StringSession(session), API_ID2, API_HASH2, system_version='4.16.30-vxCUSTOM', device_model='aboba-windows-custom', app_version='1.1.0')

@client.on(events.NewMessage)
async def my_event(event):
    global last
    log = await client.get_entity(-1002357683604)
    bot = await client.get_entity('t.me/EpsilionWarBot')
    profile = cursor.execute('SELECT * FROM users WHERE user_id = ?', (1776244625,)).fetchone()
    farm_location = profile[5]
    farm_locations = "💦 Сквозь водопад 🌿 Заросли 💧 Спуск к воде 🏖 Побережье"
    state1 = profile[3]
    state2 = profile[4]
    if str(event.message.from_id) == "PeerUser(user_id=1776244625)":
        if event.message.text == "/start_cup_up" and state1 == 1:
            await client.send_message(log, "Сессия уже запущена.")
        if event.message.text == "/start_cup_up" and state1 == 0:
            cursor.execute('UPDATE users SET state1 = ? WHERE user_id = ?', (1, 1776244625,))
            connection.commit()
            await asyncio.sleep(1)
            await client.send_message(log, "Сессия успешно запущена.")
            await cup_up()
        if event.message.text == "/stop_cup_up" and state1 == 0:
            await client.send_message(log, "Сессия уже остановлена.")
        if event.message.text == "/stop_cup_up" and state1 == 1:
            cursor.execute('UPDATE users SET state1 = ? WHERE user_id = ?', (0, 1776244625,))
            connection.commit()
            await client.send_message(log, "Сессия успешно остановлена.")
        
        
        if event.message.text == "/start_farm" and state2 == 0 or state2 == 2:
            cursor.execute('UPDATE users SET state2 = ? WHERE user_id = ?', (1, 1776244625,))
            connection.commit()
            await client.send_message(log, "Вы успешно начали фармить.")
            await asyncio.sleep(1)
            await client.send_message(await client.get_entity('t.me/EpsilionWarBot'), "⚔️ Найти врагов")
        if event.message.text == "/start_farm" and state2 == 1:
            await client.send_message(log, "Вы уже фармите.")
        if event.message.text == "/stop_farm" and state2 == 1 or state2 == 2:
            cursor.execute('UPDATE users SET state2 = ? WHERE user_id = ?', (0, 1776244625,))
            connection.commit()
            await client.send_message(log, "Вы успешно закончили фармить.")
        if event.message.text == "/stop_farm" and state2 == 0:
            await client.send_message(log, "Вы уже не фармите.")
        if "/set_location" in event.message.text:
            try:
                if event.message.text.split(" ")[0] == "/set_location":
                    await client.send_message(log, await set_farm_location(event.message.text.split("set_location ")[1]))
            except:
                await client.send_message(log, "Смена локации не удалась.")
        
        
    try:
        text = event.message.text
    except:
        pass
    if "Экипировка" in text and "снята из-за поломки" in text and str(event.message.peer_id) == "PeerUser(user_id=776510403)" and state2 == 1:
            cursor.execute('UPDATE users SET state2 = ? WHERE user_id = ?', (0, 1776244625,))
            connection.commit()
            await client.send_message(log, "Фарм приостановлен из за поломки экипировки")
            await client.forward_messages(log, event.message.id, bot)
    await asyncio.sleep(1)
    profile = cursor.execute('SELECT * FROM users WHERE user_id = ?', (1776244625,)).fetchone()
    state2 = profile[4]
    hp1 = profile[6]
    hp2 = profile[7]


    if str(event.message.peer_id) == "PeerUser(user_id=776510403)" and state2 == 1:
        text = event.message.text
        text2 = None
        keyboard = str(event.message.reply_markup)
        if "🤴️[ВатаХряка](tg://user?id=1776244625) 🔸27 ❤️" in text:
            hp1 = int(text.split("🤴️[ВатаХряка](tg://user?id=1776244625) 🔸27 ❤️(")[1].split(")")[0].split("/")[0])
            hp2 = int(text.split("🤴️[ВатаХряка](tg://user?id=1776244625) 🔸27 ❤️(")[1].split(")")[0].split("/")[1])
            cursor.execute('UPDATE users SET hp1 = ? WHERE user_id = ?', (hp1, 1776244625,))
            cursor.execute('UPDATE users SET hp2 = ? WHERE user_id = ?', (hp2, 1776244625,))
            connection.commit()
        if "Текущее здоровье:" in text:
            hp1 = int(text.split("❤️ (")[1].split(")")[0].split("/")[0])
            hp2 = int(text.split("❤️ (")[1].split(")")[0].split("/")[1])
            cursor.execute('UPDATE users SET hp1 = ? WHERE user_id = ?', (hp1, 1776244625,))
            cursor.execute('UPDATE users SET hp2 = ? WHERE user_id = ?', (hp2, 1776244625,))
            connection.commit()
            if hp2-hp1<=hp2/2:
                await asyncio.sleep(5)
                text2 = "⚔️ Найти врагов"
        if "В голову" in keyboard and "(0/" not in text:
            kombo = random.randint(1, 5)
            if kombo == 1:
                text2 = "В голову"
            if kombo == 2:
                text2 = "В грудь"
            if kombo == 3:
                text2 = "В живот"
            if kombo == 4:
                text2 = "В пояс"
            if kombo == 5:
                text2 = "В ноги"
        elif "Голову, грудь, живот" in keyboard:
            kombo = random.randint(1, 5)
            if kombo == 1:
                text2 = "Голову, грудь, живот"
            if kombo == 2:
                text2 = "Грудь, живот, пояс"
            if kombo == 3:
                text2 = "Живот, пояс, ноги"
            if kombo == 4:
                text2 = "Пояс, ноги, голова"
            if kombo == 5:
                text2 = "Ноги, голова, грудь"
        elif "🥪 Бутерброд [III]" in keyboard and hp2-hp1>=300  and "(0/" not in text:
            text2 = "🥪 Бутерброд [III]"
        elif "🍞 Корка хлеба [II]" in keyboard and hp2-hp1>=75  and "(0/" not in text:
            text2 = "🍞 Корка хлеба [II]"
        elif "Древняя регенерация (1🗡)" in keyboard and hp2-hp1>=100 and "(0/" not in text:
            text2 = "Древняя регенерация (1🗡)"
        elif "Внутренняя сила (2🗡; 3🛡)" in keyboard  and "(0/" not in text:
            text2 = "Внутренняя сила (2🗡; 3🛡)"
        elif "По наитию (3 🥊)" in keyboard and "(0/" not in text:
            text2 = "По наитию (3 🥊)"
        elif "Точный выпад (1🥊; 2🛡;1 🌬)" in keyboard and "(0/" not in text:
            text2 = "Точный выпад (1🥊; 2🛡;1 🌬)"
        elif "Активная защита (3 🛡)" in keyboard and "(0/" not in text:
            text2 = "Активная защита (3 🛡)"
        elif "Пропустить" in keyboard and "(0/" not in text:
            text2 = "Пропустить"
        elif "⚔️ Найти врагов" in keyboard and hp2-hp1<hp2/2:
            await asyncio.sleep(5)
            state2 = cursor.execute('SELECT * FROM users WHERE user_id = ?', (1776244625,)).fetchone()[4]
            if state2 == 1:
                text2 = "⚔️ Найти врагов"
        elif "⚔️ Найти врагов" in keyboard and hp2-hp1>=hp2/2:
            text2 = "/use_middle_hpIII"
        elif "Ваше здоровье полностью восстановлено" in text:
            text2 = "⚔️ Найти врагов"
        elif text == "Неверно, будь аккуратнее или попадешь в тюрьму":
            await asyncio.sleep(10)
            cursor.execute('UPDATE users SET state2 = ? WHERE user_id = ?', (2, 1776244625,))
            connection.commit()
            await client.send_message(await client.get_entity('t.me/gpt3_unlim_chatbot'), f"{last}\n\nПиши только ответ и ничего больше. \nгород Ц*рта=Цирта М*ледон=Миледон 🐺=волк п*тница=пятнциа и*ль=июль коло*ец=колодец *обака=собака столица Эпсилиона=Миледон 🍌=банан 🤡= клоун *оябрь=ноябрь")
            await asyncio.sleep(10)
            await client.send_message(await client.get_entity('t.me/gpt3_unlim_chatbot'), "Очистить историю диалога")
        elif "Ты отправлен в тюрьму" in text:
            await client.send_message(bot, "3")
            await client.send_message(bot, "🗺Карта")
            await asyncio.sleep(3)
            await client.send_message(bot, "🏛 Цирта")
            await asyncio.sleep(60)
            await client.send_message(log, f"Вы попали в тюрьму \n\n{last}")
            await client.send_message(bot, "2")
        elif "Ты победил своего врага" in text:
            text2 = "✅ Забрать нaграду"
            await client.forward_messages(log, event.message.id, bot)
        elif "попытался сбежать" in text and "В зону охоты" in keyboard:
            text2 = "В зону охоты"
            await client.forward_messages(log, event.message.id, bot)
        try:
            if str(text.split(" ")[1].replace("*", "")).split("\n")[0] == "Цирта":
                await client.send_message(bot, "🏡🏛 Грейт-Йелдем")
            if str(text.split(" ")[1].replace("*", "")).split("\n")[0] == "Грейт-Йелдем":
                if farm_location in farm_locations:
                    await client.send_message(bot, "🏞🏛 Озеро Эпсил")
                else:
                    await client.send_message(bot, "⚓🏛 Чёртова бухта")
            elif str(text.split(" ")[1].replace("*", "")).split("\n")[0] != farm_location.split(" ")[1] and farm_location in keyboard:
                await client.send_message(bot, farm_location)
        except:
            pass
        try:
            if text.split(".")[0] == "На пути ты встретил капчу":
                cursor.execute('UPDATE users SET state2 = ? WHERE user_id = ?', (2, 1776244625,))
                connection.commit()
                await client.send_message(await client.get_entity('t.me/gpt3_unlim_chatbot'), f"{text}\n\nПиши только ответ и ничего больше. \nгород Ц*рта=Цирта М*ледон=Миледон 🐺=волк п*тница=пятнциа и*ль=июль коло*ец=колодец *обака=собака столица Эпсилиона=Миледон 🍌=банан 🤡= клоун *оябрь=ноябрь")
                last = text
                await asyncio.sleep(10)
                await client.send_message(await client.get_entity('t.me/gpt3_unlim_chatbot'), "Очистить историю диалога")
                await client.send_message(await client.get_entity('t.me/gpt3_unlim_chatbot'), "Reset dilog history")
        except:
            pass
        try:
            if "Ты отправляешься в ближайший город на восстановление" in text or "Ты был отправлен восстанавливаться в город" in text:
                await client.send_message(bot, farm_location)
                await client.forward_messages(log, event.message.id, bot)
        except:
            pass
        if text2 != None:
            await client.send_message(bot, text2)
    if str(event.message.peer_id) == "PeerUser(user_id=5815596965)" and state2 == 2:
        cursor.execute('UPDATE users SET state2 = ? WHERE user_id = ?', (1, 1776244625,))
        connection.commit()
        await client.send_message(bot, event.message.text)
            

async def set_farm_location(location):
    cursor.execute('UPDATE users SET farm_location = ? WHERE user_id = ?', (location, 1776244625,))
    connection.commit()
    return(f"Успешно задана локация {location}.")

async def set_minhp(hp):
    cursor.execute('UPDATE users SET minhp = ? WHERE user_id = ?', (hp, 1776244625,))
    connection.commit()
    return(f"Успешно задано минимальное хп {hp}.")

async def cup_up():
    state1 = cursor.execute('SELECT * FROM users WHERE user_id = ?', (1776244625,)).fetchone()[3]
    while state1 == 1:
        bot1 = await client.get_entity('t.me/CupLegendBot')
        await client.send_message(bot1, "/cup_up")
        await asyncio.sleep(310)
        state1 = cursor.execute('SELECT * FROM users WHERE user_id = ?', (1776244625,)).fetchone()[3]



import asyncio
import logging
import sqlite3

from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.types import Message, InlineKeyboardButton, WebAppInfo, CallbackQuery, ChosenInlineResult
from aiogram.utils.keyboard import InlineKeyboardBuilder

BOT_TOKEN = '7775440771:AAFLb1IJg1gOoQmnhNosUKkvg0eG_VC_YPg'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)
connection2 = sqlite3.connect("RP.db")
cursor2 = connection2.cursor()
cursor2.execute(
    """CREATE TABLE IF NOT EXISTS msg(
id INTEGER PRIMARY KEY,
username INT,
text STR,
sender INT
)
""")


rp_commands = ["пнуть", "обнять", "поцеловать", "ударить", "погладить","укусить", "защекотать", "поколотить", "побить","похлопать по плечу", "пожать руку", "схватить за руку", "потянуть за руку","постучать по голове", "потереть голову", "погладить по спине", "погладить по щеке", "поцеловать в щеку", "поцеловать в лоб","поцеловать в губы", "закричать на", "прошептать на ушко", "попросить прощения у", "поблагодарить", "подмигнуть","улыбнуться", "нахмуриться", "показать язык", "отвернуться от","спрятаться за", "подойти к", "отойти от", "посмотреть на","помахать рукой", "показать кулак", "сделать предложение","завязать шнурки", "дать попить", "дать поесть","забрать еду", "убить", "сделать комплимент", "сказать спасибо","сказать пожалуйста", "попросить помощи", "пригласить на свидание", "подарить цветок", "подарить подарок", "попросить телефон","сделать фото", "потанцевать с", "спеть песню для", "рассказать анекдот", "поделиться секретом", "спросить совета"]

@dp.message(F.text)
async def handle_rp_command(message: Message):
  if(message.text.split("™")[0] == "app"):
        await message.answer(message.text.split("™")[1], reply_markup=InlineKeyboardBuilder().add(InlineKeyboardButton(text=message.text.split("™")[2], web_app=WebAppInfo(url=message.text.split("™")[3]))).as_markup())
        await message.delete()
  reply_to_message = message.reply_to_message
  if reply_to_message:
    user_mention = message.from_user.full_name
    reply_user_mention = reply_to_message.from_user.full_name
    action = message.text.lower()
    if action == "/delete" and str(message.from_user.id) == "1776244625":
        await message.delete()
        await asyncio.sleep(10)
        await reply_to_message.delete()
    if action == "/delete_long" and str(message.from_user.id) == "1776244625":
        await message.delete()
        await asyncio.sleep(60)
        await reply_to_message.delete()
    if " " in action:
        if action.split(" ")[0] == "/delete_all" and str(message.from_user.id) == "1776244625":
            await message.delete()
            await asyncio.sleep(1)
            id = message.reply_to_message.message_id
            chat_id = message.chat.id
            i = int(action.split(" ")[1])
            while i != 0:
                try:
                    await bot.delete_message(chat_id, id)
                    id = int(id)-1
                    i = i-1
                except:
                    id = int(id)-1
                await asyncio.sleep(2)
        if action.split(" ")[0] == "/mrp" and str(message.from_user.id) == "1776244625":
            li = list(message.text)
            li[0] = ''
            li[1] = ''
            li[2] = ''
            li[3] = ''
            li[4] = ''
            text = ''.join(li)
            if message.reply_to_message == None:
                await message.answer(text)
                await message.delete()
            else:
                await message.reply_to_message.reply(text)
                await message.delete()


    if action in rp_commands :
        await message.delete()

    if action == "пнуть":
      text = f"Обезьяна по имени {user_mention} пнула обезьяну по имени {reply_user_mention}"
    elif action == "обнять":
      text = f"Обезьяна по имени {user_mention} обняла обезьяну по имени {reply_user_mention}"
    elif action == "поцеловать":
      text = f"Обезьяна по имени {user_mention} поцеловала обезьяну по имени {reply_user_mention}"
    elif action == "ударить":
      text = f"Обезьяна по имени {user_mention} ударила обезьяну по имени {reply_user_mention}"
    elif action == "погладить":
      text = f"Обезьяна по имени {user_mention} погладила обезьяну по имени {reply_user_mention}"
    elif action == "укусить":
        text = f"Обезьяна по имени {user_mention} укусила обезьяну по имени {reply_user_mention}"
    elif action == "защекотать":
        text = f"Обезьяна по имени {user_mention} защекотала обезьяну по имени {reply_user_mention}"
    elif action == "поколотить":
        text = f"Обезьяна по имени {user_mention} поколотила обезьяну по имени {reply_user_mention}"
    elif action == "побить":
         text = f"Обезьяна по имени {user_mention} побила обезьяну по имени {reply_user_mention}"
    elif action == "похлопать по плечу":
        text = f"Обезьяна по имени {user_mention} похлопала по плечу обезьяну по имени {reply_user_mention}"
    elif action == "пожать руку":
        text = f"Обезьяна по имени {user_mention} пожала руку обезьяне по имени {reply_user_mention}"
    elif action == "схватить за руку":
        text = f"Обезьяна по имени {user_mention} схватила за руку обезьяну по имени {reply_user_mention}"
    elif action == "потянуть за руку":
        text = f"Обезьяна по имени {user_mention} потянула за руку обезьяну по имени {reply_user_mention}"
    elif action == "постучать по голове":
        text = f"Обезьяна по имени {user_mention} постучала по голове обезьяну по имени {reply_user_mention}"
    elif action == "потереть голову":
        text = f"Обезьяна по имени {user_mention} потерла голову обезьяне по имени {reply_user_mention}"
    elif action == "погладить по спине":
        text = f"Обезьяна по имени {user_mention} погладила по спине обезьяну по имени {reply_user_mention}"
    elif action == "погладить по щеке":
        text = f"Обезьяна по имени {user_mention} погладила по щеке обезьяну по имени {reply_user_mention}"
    elif action == "поцеловать в щеку":
        text = f"Обезьяна по имени {user_mention} поцеловала в щеку обезьяну по имени {reply_user_mention}"
    elif action == "поцеловать в лоб":
        text = f"Обезьяна по имени {user_mention} поцеловала в лоб обезьяну по имени {reply_user_mention}"
    elif action == "поцеловать в губы":
        text = f"Обезьяна по имени {user_mention} поцеловала в губы обезьяну по имени {reply_user_mention}"
    elif action == "закричать на":
        text = f"Обезьяна по имени {user_mention} закричала на обезьяну по имени {reply_user_mention}"
    elif action == "прошептать на ушко":
        text = f"Обезьяна по имени {user_mention} прошептала на ушко обезьяне по имени {reply_user_mention}"
    elif action == "попросить прощения у":
        text = f"Обезьяна по имени {user_mention} попросила прощения у обезьяны по имени {reply_user_mention}"
    elif action == "поблагодарить":
        text = f"Обезьяна по имени {user_mention} поблагодарила обезьяну по имени {reply_user_mention}"
    elif action == "подмигнуть":
        text = f"Обезьяна по имени {user_mention} подмигнула обезьяне по имени {reply_user_mention}"
    elif action == "улыбнуться":
        text = f"Обезьяна по имени {user_mention} улыбнулась обезьяне по имени {reply_user_mention}"
    elif action == "нахмуриться":
        text = f"Обезьяна по имени {user_mention} нахмурилась на обезьяну по имени {reply_user_mention}"
    elif action == "показать язык":
        text = f"Обезьяна по имени {user_mention} показала язык обезьяне по имени {reply_user_mention}"
    elif action == "отвернуться от":
        text = f"Обезьяна по имени {user_mention} отвернулась от обезьяны по имени {reply_user_mention}"
    elif action == "спрятаться за":
        text = f"Обезьяна по имени {user_mention} спряталась за обезьяну по имени {reply_user_mention}"
    elif action == "подойти к":
        text = f"Обезьяна по имени {user_mention} подошла к обезьяне по имени {reply_user_mention}"
    elif action == "отойти от":
        text = f"Обезьяна по имени {user_mention} отошла от обезьяны по имени {reply_user_mention}"
    elif action == "посмотреть на":
        text = f"Обезьяна по имени {user_mention} посмотрела на обезьяну по имени {reply_user_mention}"
    elif action == "помахать рукой":
        text = f"Обезьяна по имени {user_mention} помахала рукой обезьяне по имени {reply_user_mention}"
    elif action == "показать кулак":
        text = f"Обезьяна по имени {user_mention} показала кулак обезьяне по имени {reply_user_mention}"
    elif action == "сделать предложение":
        text = f"Обезьяна по имени {user_mention} сделала предложение обезьяне по имени {reply_user_mention}"
    elif action == "завязать шнурки":
        text = f"Обезьяна по имени {user_mention} завязала шнурки обезьяне по имени {reply_user_mention}"
    elif action == "дать попить":
        text = f"Обезьяна по имени {user_mention} дала попить обезьяне по имени {reply_user_mention}"
    elif action == "дать поесть":
        text = f"Обезьяна по имени {user_mention} дала поесть обезьяне по имени {reply_user_mention}"
    elif action == "забрать еду":
        text = f"Обезьяна по имени {user_mention} забрала еду у обезьяны по имени {reply_user_mention}"
    elif action == "убить":
        text = f"Обезьяна по имени {user_mention} убила обезьяну по имени {reply_user_mention}"
    elif action == "сделать комплимент":
        text = f"Обезьяна по имени {user_mention} сделала комплимент обезьяне по имени {reply_user_mention}"
    elif action == "сказать спасибо":
        text = f"Обезьяна по имени {user_mention} сказала спасибо обезьяне по имени {reply_user_mention}"
    elif action == "сказать пожалуйста":
        text = f"Обезьяна по имени {user_mention} сказала пожалуйста обезьяне по имени {reply_user_mention}"
    elif action == "попросить помощи":
        text = f"Обезьяна по имени {user_mention} попросила помощи у обезьяны по имени {reply_user_mention}"
    elif action == "пригласить на свидание":
        text = f"Обезьяна по имени {user_mention} пригласила на свидание обезьяну по имени {reply_user_mention}"
    elif action == "подарить цветок":
        text = f"Обезьяна по имени {user_mention} подарила цветок обезьяне по имени {reply_user_mention}"
    elif action == "подарить подарок":
        text = f"Обезьяна по имени {user_mention} подарила подарок обезьяне по имени {reply_user_mention}"
    elif action == "попросить телефон":
        text = f"Обезьяна по имени {user_mention} попросила телефон у обезьяны по имени {reply_user_mention}"
    elif action == "сделать фото":
        text = f"Обезьяна по имени {user_mention} сделала фото с обезьяной по имени {reply_user_mention}"
    elif action == "потанцевать с":
        text = f"Обезьяна по имени {user_mention} потанцевала с обезьяной по имени {reply_user_mention}"
    elif action == "спеть песню для":
        text = f"Обезьяна по имени {user_mention} спела песню для обезьяны по имени {reply_user_mention}"
    elif action == "рассказать анекдот":
        text = f"Обезьяна по имени {user_mention} рассказала анекдот обезьяне по имени {reply_user_mention}"
    elif action == "поделиться секретом":
        text = f"Обезьяна по имени {user_mention} поделилась секретом с обезьяной по имени {reply_user_mention}"
    elif action == "спросить совета":
        text = f"Обезьяна по имени {user_mention} спросила совета у обезьяны по имени {reply_user_mention}"

    if action in rp_commands :
        await reply_to_message.answer(text)

def db():
    id = cursor2.execute("SELECT id FROM msg ORDER BY id DESC LIMIT 1").fetchall()
    try:
        return(f"msg_{str(id).split('(')[1].split(',')[0]}")
    except:
        return("None")

@dp.inline_query()
async def inline_callback(inline: types.InlineQuery):
    results = []
    tryy = 0
    try:
        username = inline.query.split(" ")[0]
        if username[0] != '@':
            tryy = 1
        li = list(inline.query)
        li[len(username)] = '™'
        text0 = ''.join(li)
        text1 =  text0.split("™")[1]
        if len(text1) > 200:
            tryy = 1
    except:
        tryy = 1
    if(tryy == 0):
        results.append(types.InlineQueryResultArticle(
            id='1',
            title=f"Написать сообщение {username}.",
            input_message_content=types.InputTextMessageContent(
                message_text=f"Подождите 3 секундочки... \nПожалуйста...",
            ),
            reply_markup=InlineKeyboardBuilder().add(InlineKeyboardButton(text="Подождите 3 секунды...", callback_data=db())).as_markup()
        ))
    else:
        results.append(types.InlineQueryResultArticle(
            id='1',
            title=f"Неправильные данные *click*",
            input_message_content=types.InputTextMessageContent(
                message_text='Пишите например так: \n@V_RP_BOT @Mishi5782 Ты обезьяна \n@V_RP_BOT @{username} {text} \nТак же помните, что количество символов не должно превышать 200 символов.',
            ),
        ))
    await inline.answer(
        results=results,
        button=types.InlineQueryResultsButton(
            text='_RP_',
            start_parameter='fromInline',
        ),
        cache_time=2,
    )

@dp.callback_query()
async def callback(callback: CallbackQuery):
    data = callback.data
    if data.split("_")[0] == "msg":
        try:
            text = str(cursor.execute("SELECT text FROM msg WHERE id = ?", (data.split("_")[1],)).fetchone()).split("'")[1]
            username = str(cursor.execute("SELECT username FROM msg WHERE id = ?", (data.split("_")[1],)).fetchone()).split("'")[1]
            if f"@{callback.from_user.username}" == username or str(callback.from_user.id) == "1776244625":
                await callback.answer(text, show_alert=True)
            else:
                await callback.answer(f"Это сообщение может прочитать только {username}", show_alert=True)
        except:
            await callback.answer("Произошла ошибка!", show_alert=True)

@dp.chosen_inline_result()
async def inline_result(inline: ChosenInlineResult):
    tryy = 0
    try:
        username = inline.query.split(" ")[0]
        if username[0] != '@':
            tryy = 1
        li = list(inline.query)
        li[len(username)] = '™'
        text0 = ''.join(li)
        text1 =  text0.split("™")[1]
        if len(text1) > 200:
            tryy = 1
    except:
        tryy = 1
    if tryy == 0:
        await asyncio.sleep(3)
        cursor2.execute("INSERT INTO msg (username, text, sender) VALUES (?, ?, ?)", (username, text1, f"@{inline.from_user.username}",))
        connection2.commit()
        msg_id = inline.inline_message_id
        await bot.edit_message_text(text=f"Это сообщение может прочитать только {username}", inline_message_id=msg_id)
        await bot.edit_message_reply_markup(reply_markup=InlineKeyboardBuilder().add(InlineKeyboardButton(text="_Прочитать сообщение_", callback_data=db())).as_markup(), inline_message_id=msg_id)




if __name__ == '__main__':
    client.start()
    client.run_until_disconnected()
    asyncio.run(main())

async def main():
    await dp.start_polling(bot)
