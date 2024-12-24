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

connection = sqlite3.connect("farm.db")
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
hp2 INT,
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
        
        
        if event.message.text == "/start_farm" and state2 == 0:
            cursor.execute('UPDATE users SET state2 = ? WHERE user_id = ?', (1, 1776244625,))
            connection.commit()
            await client.send_message(log, "Вы успешно начали фармить.")
            await asyncio.sleep(1)
            await client.send_message(await client.get_entity('t.me/EpsilionWarBot'), "⚔️ Найти врагов")
        if event.message.text == "/start_farm" and state2 == 1:
            await client.send_message(log, "Вы уже фармите.")
        if event.message.text == "/stop_farm" and state2 == 1:
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
    await asyncio.sleep(2)
    profile = cursor.execute('SELECT * FROM users WHERE user_id = ?', (1776244625,)).fetchone()
    state2 = profile[4]
    hp1 = profile[6]
    hp2 = profile[7]


    if str(event.message.peer_id) == "PeerUser(user_id=776510403)" and state2 == 1:
        text = event.message.text
        text2 = None
        keyboard = str(event.message.reply_markup)
        if "🤴️[ВатаХряка](tg://user?id=1776244625) 🔸25 ❤️" in text:
            hp1 = int(text.split("🤴️[ВатаХряка](tg://user?id=1776244625) 🔸25 ❤️(")[1].split(")")[0].split("/")[0])
            hp2 = int(text.split("🤴️[ВатаХряка](tg://user?id=1776244625) 🔸25 ❤️(")[1].split(")")[0].split("/")[1])
            cursor.execute('UPDATE users SET hp1 = ? WHERE user_id = ?', (hp1, 1776244625,))
            cursor.execute('UPDATE users SET hp2 = ? WHERE user_id = ?', (hp2, 1776244625,))
            connection.commit()
        if "Текущее здоровье:" in text:
            hp1 = int(text.split("❤️ (")[1].split(")")[0].split("/")[0])
            hp2 = int(text.split("❤️ (")[1].split(")")[0].split("/")[1])
            cursor.execute('UPDATE users SET hp1 = ? WHERE user_id = ?', (hp1, 1776244625,))
            cursor.execute('UPDATE users SET hp2 = ? WHERE user_id = ?', (hp2, 1776244625,))
            connection.commit()
            if hp2-hp1<=1000:
                text2 = "⚔️ Найти врагов"
        if "В голову" in keyboard:
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
        elif "🥪 Бутерброд [III]" in keyboard and hp2-hp1>=300:
            text2 = "🥪 Бутерброд [III]"
        elif "🍞 Корка хлеба [II]" in keyboard and hp2-hp1>=75:
            text2 = "🍞 Корка хлеба [II]"
        elif "Древняя регенерация (1🗡)" in keyboard and hp2-hp1>=100:
            text2 = "Древняя регенерация (1🗡)"
        elif "Внутренняя сила (2🗡; 3🛡)" in keyboard:
            text2 = "Внутренняя сила (2🗡; 3🛡)"
        elif "По наитию (3 🥊)" in keyboard:
            text2 = "По наитию (3 🥊)"
        elif "Точный выпад (1🥊; 2🛡;1 🌬)" in keyboard:
            text2 = "Точный выпад (1🥊; 2🛡;1 🌬)"
        elif "Активная защита (3 🛡)" in keyboard:
            text2 = "Активная защита (3 🛡)"
        elif "Пропустить" in keyboard:
            text2 = "Пропустить"
        elif "⚔️ Найти врагов" in keyboard and hp2-hp1<=1000:
            text2 = "⚔️ Найти врагов"
        # elif "⚔️ Найти врагов" in keyboard and hp2-hp1>=hp2/2:
        #     text2 = "/use_middle_hpIII"
        elif "Ваше здоровье полностью восстановлено" in text:
            text2 = "⚔️ Найти врагов"
        elif text == "Неверно, будь аккуратнее или попадешь в тюрьму":
            await asyncio.sleep(10)
            cursor.execute('UPDATE users SET state2 = ? WHERE user_id = ?', (2, 1776244625,))
            connection.commit()
            await client.send_message(await client.get_entity('t.me/gpt3_unlim_chatbot'), f"{last}\n\nПиши только ответ и ничего больше. \nЦ*рта=Цирта М*ледон=Миледон 🐺=волк п*тница=пятнциа и*ль=июль коло*ец=колодец *обака=собака столица Эпсилиона=Миледон 🍌=банан 🤡= клоун")
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
            if str(text.split(" ")[1].replace("*", "")).split("\n")[0] == str(farm_location).split(" ")[1]:
                if hp1<=hp2/10:
                    text2 = "/use_great_hp"
                elif hp1<=hp2/2:
                    text2 = "/use_middle_hpIII"
        except:
            pass
        try:
            if text.split(".")[0] == "На пути ты встретил капчу":
                cursor.execute('UPDATE users SET state2 = ? WHERE user_id = ?', (2, 1776244625,))
                connection.commit()
                await client.send_message(await client.get_entity('t.me/gpt3_unlim_chatbot'), f"{text}\n\nПиши только ответ и ничего больше. \nЦ*рта=Цирта М*ледон=Миледон 🐺=волк п*тница=пятнциа и*ль=июль коло*ец=колодец *обака=собака столица Эпсилиона=Миледон 🍌=банан 🤡= клоун")
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


if __name__ == '__main__':
    client.start()
    client.run_until_disconnected()
