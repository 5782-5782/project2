import telethon
import logging
import sqlite3
import asyncio
import time
from telethon.sync import TelegramClient, events
from telethon.sessions import StringSession

API_ID=23371011
API_HASH='065c5c8afeb1287e38eb2c457fcfdfd8'
SESSION = '1ApWapzMBu2l1JOL4TH737z_Ocq_Js7SEIaz28SkHJNph_AMD_pwrFkuvLWOTvNBkpuOQYHrTyArIKlVGhSOb8gcGRPAWbm3djT7fr1nIwrr8RT8R6lFlccMeyjNgbfn78J06oPNPOcuNDt2TVzeccK3d0ddzG6fgVmhbf0QcLEYf5BODeCxZ2n2-SFWWmYJLwqXiQ8GXT1ldRkU50NR-3Bw4oF189JQezO8OVWIxVfcCGeYLKzDaZQX9QMBFTvEsMpJD5Uu8cdls_zF8pK_zXwltlZqKeN_OmTdLYubBYXWGlES0sZbyPEbbNYmLWE-S0qYNcxJGQB6L4y8ecNxF2Dx7DqXY2Ns='

logging.basicConfig(level=logging.INFO)

client = TelegramClient(StringSession(SESSION), API_ID, API_HASH, system_version='4.16.30-vxCUSTOM', device_model='aboba-windows-custom', app_version='1.1.0')
pers=[]

state=0
tume=200

async def pon():
    global state, pers
    bot = await client.get_entity('CupLegendBot')
    i = 0
    perso = ["Пудель2", "Пудель3", "Пудель4", "Пудель5", "Пудель6", "Пудель7", "Пудель8", "Пудель9", "Пудель10", "Пудель"]
    await client.send_message(bot, "ВНИМАНИЕ!!!!\nНЕ ИСПОЛЬЗУЙТЕ БОТА НИКАКИМ ОБРАЗОМ ПО КРАЙНЕЙ МЕРЕ 2-3 МИНУТЫ!!!!\nНЕ НАЖИМАЙТЕ КНОПКИ И НЕ ПИШИТЕ ЛЮБЫЕ СООБЩЕНИЯ БОТУ!!!\nЕСЛИ ВЫ СЛУЧАЙНО ЭТО СДЕЛАЛИ, ПЕРЕЗАПУСТИТЕ СКРИПТ!!!")
    await asyncio.sleep(1)
    while i < 10:
        if state==1:
            await client.send_message(bot, "/start MyHeros")
            await asyncio.sleep(1)
            msgs = await client.get_messages('CupLegendBot', 1)
            msg = msgs[0]
            await msg.click(text=perso[i])
            msgs = await client.get_messages('CupLegendBot', 1)
            pers.append(msgs[0])
            await asyncio.sleep(1)
        i = i+1


@client.on(events.NewMessage)
async def my_event(event):
    global state
    if event.message.text=="/start_cup" and state==0:
        state=1
        await pon()
        await cup_up()
    if event.message.text=="/stop_cup" and state==1:
        state=0


async def cup_up():
    global state, tume
    i=9
    while state==1:
        i=i+1
        date1=int(time.time())
        await cup_up2()
        date2=int(time.time())
        date=date2-date1
        print(date)
        await asyncio.sleep(tume+3-date)
        if i==10:
            i=0
            bot = await client.get_entity('CupLegendBot')
            await client.send_message(bot, "/cup_up")
            await asyncio.sleep(1)
            await client.send_message(bot, "/cup_up")
            msgs = await client.get_messages('CupLegendBot', 1)
            msg=msgs[0]
            try:
                tume=int(msg.text.split("Подожди ещё 00:")[1].split(":")[0])*60+int(msg.text.split("Подожди ещё 00:")[1].split(".")[0].split(":")[1])
            except:
                print("error")
                tume=250
                i=9
            

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
