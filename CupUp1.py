import logging
import asyncio
import time
from telethon.sync import TelegramClient, events
from telethon.sessions import StringSession

API_ID=25980590
API_HASH='1d281e8e6c14983eecc5aadabf981137'
SESSION   = '1ApWapzMBu8PQ-AH74JwzGiDk-8szOKAgE-gX9NikTKSRXwY-MQzXAHZ53UWPmcJL51fJ9nOqaVhDikTfmGaHH7wFiyXiyu1jcBV-rTd3yjpblZl5mAy5cSqnNzJ7W50FpC7pEX95sf0gZp664G5mvGMXaJwdzPP4JjWlz7vBRqcsoy_fs_aP2iQKYSoe-vz1fPQodrzLHK9bz-3Ll00Rc4nYncesTTSXUqp7jTbXoLoGYYyRdLF0LbJpvKhl6hnaoa-Ne1QFCoCCAY-rDo2uox2iMYb9Js72XOaG2I72y1G-tozPkg9I8jy2dLMv_mvOtLg3nIas9FL-fo4czEEGaFQ2Ql00BGM='

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
    perso = ["MORGENSHTERN", "Леон", "Крейзи", "Голубь", "Ямаль", "Карти", "Тиг", "Слитые", "Биток", "Легенд"]
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
