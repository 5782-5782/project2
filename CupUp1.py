import logging
import asyncio
import time
from telethon.sync import TelegramClient, events
from telethon.sessions import StringSession

API_ID=23473442
API_HASH='0cd1d983e8b65e8d992b3b756f9a8eb1'
SESSION = '1ApWapzMBu2Uk4Hp0Dqd4ldUu8GFEmdHQ5zD6pbfsQQsIVG5Rj-seeoOb7frP90rMSQERLRJ4bfIxcclM8KPO6rZ72bkXxAWqS73ZHUGdGCthAeZ9o-UOUziuByOa4pbVDcAoKwAj9cjS0JE3SjKzTtPwc0TlkZUoPz0ypQ4zHIC1QDu7t7B_INbLgq2SD11159aVXPnU6-yabzqA12BmZPyrLRQvQfE0nENrhg81Yrtt7OnILwghPxRIPTNG5St7Fd36_wraJfd-o--KxMerI6fNk1YfYb3O8Qg1MnCBMrixnFQUtRAFh68lXlVU2nXZF9E4G06C9N1r6iKO_d5OY45vucBWJ90='

logging.basicConfig(level=logging.INFO)

client = TelegramClient(StringSession(SESSION), API_ID, API_HASH, system_version='4.16.30-vxCUSTOM', device_model='aboba-windows-custom', app_version='1.1.0')
pers=[]

state=0
tume=132

async def pon():
    global state, pers
    pers=[]
    bot = await client.get_entity('CupLegendBot')
    i = 0
    perso = ["Пудель2", "Пудель3", "Пудель4", "Пудель5", "Пудель6", "Пудель7", "Пудель8", "Пудель9", "Пудель10", "Пудель"]
    await client.send_message(bot, "ВНИМАНИЕ!!!!\nНЕ ИСПОЛЬЗУЙТЕ БОТА НИКАКИМ ОБРАЗОМ ПО КРАЙНЕЙ МЕРЕ 2-3 МИНУТЫ!!!!\nНЕ НАЖИМАЙТЕ КНОПКИ И НЕ ПИШИТЕ ЛЮБЫЕ СООБЩЕНИЯ БОТУ!!!\nЕСЛИ ВЫ СЛУЧАЙНО ЭТО СДЕЛАЛИ, ПЕРЕЗАПУСТИТЕ СКРИПТ!!!")
    await asyncio.sleep(1)
    while i < 10:
        if state==1:
            await client.send_message(bot, "/start MyHeros")
            await asyncio.sleep(5)
            msgs = await client.get_messages('CupLegendBot', 1)
            msg = msgs[0]
            await asyncio.sleep(5)
            await msg.click(text=perso[i])
            await asyncio.sleep(5)
            msgs = await client.get_messages('CupLegendBot', 1)
            pers.append(msgs[0])
            await asyncio.sleep(5)
        i = i+1


@client.on(events.NewMessage)
async def my_event(event):
    global state
    if event.message.text=="/start_cup" and state==0 and event.message.to_dict()['from_id']['user_id']==1817889040:
        state=1
        await pon()
        await cup_up()
    if event.message.text=="/stop_cup" and state==1 and event.message.to_dict()['from_id']['user_id']==1817889040:
        state=0


async def cup_up():
    global state, tume
    while state==1:
        date1=int(time.time())
        await cup_up2()
        date2=int(time.time())
        date=date2-date1
        print(date)
        await asyncio.sleep(tume-date)
            

async def cup_up2():
    global pers
    await asyncio.sleep(1)
    bot = await client.get_entity('CupLegendBot')
    i = 0
    while i < 10:
        if state==1:
            msg = pers[i]
            await msg.click(text="Выбрать")
            await asyncio.sleep(1)
            await client.send_message(bot, "/cup_up")
            await asyncio.sleep(1)
        i = i+1



if __name__ == '__main__':
    client.start()
    client.run_until_disconnected()
