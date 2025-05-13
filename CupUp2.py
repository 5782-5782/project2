import logging
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

state2=0
state=0
tume=132

async def pon():
    global state, pers
    pers=[]
    bot = await client.get_entity('CupLegendBot')
    i = 0
    perso = ["Мэг", "Ямаль", "Трэвис Скотт", "Френки", "Луми", "Бруно", "Хави", "Старик", "Гоат", "Рафа"]
    await client.send_message(bot, "ВНИМАНИЕ!!!!\nНЕ ИСПОЛЬЗУЙТЕ БОТА НИКАКИМ ОБРАЗОМ ПО КРАЙНЕЙ МЕРЕ 2-3 МИНУТЫ!!!!\nНЕ НАЖИМАЙТЕ КНОПКИ И НЕ ПИШИТЕ ЛЮБЫЕ СООБЩЕНИЯ БОТУ!!!\nЕСЛИ ВЫ СЛУЧАЙНО ЭТО СДЕЛАЛИ, ПЕРЕЗАПУСТИТЕ СКРИПТ!!!")
    await asyncio.sleep(1)
    while i < 10:
        if state==1:
            await client.send_message(bot, "/start MyHeros")
            await asyncio.sleep(1)
            msgs = await client.get_messages('CupLegendBot', 1)
            msg = msgs[0]
            await msg.click(text=perso[i])
            await asyncio.sleep(1)
            msgs = await client.get_messages('CupLegendBot', 1)
            pers.append(msgs[0])
            await asyncio.sleep(1)
        i = i+1


@client.on(events.NewMessage)
async def my_event(event):
    global state, state2
    if state2==0:
        state2=1
        bot = await client.get_entity("F_CardBot")
        while True:
            await client.send_message(bot, "🃏 Получить карту")
            await asyncio.sleep(10860)
    if event.message.text=="/start_cup" and state==0 and event.message.to_dict()['from_id']['user_id']==6728865868:
        state=1
        await pon()
        await cup_up()
    if event.message.text=="/stop_cup" and state==1 and event.message.to_dict()['from_id']['user_id']==6728865868:
        state=0


async def cup_up():
    global state, tume
    while state==1:
        date1=int(time.time())
        await cup_up2()
        date2=int(time.time())
        date=date2-date1
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
