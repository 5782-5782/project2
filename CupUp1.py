import telethon
import logging
import sqlite3
import asyncio
import time
from telethon.sync import TelegramClient, events
from telethon.sessions import StringSession

API_ID1=25980590
API_HASH1='1d281e8e6c14983eecc5aadabf981137'
SESSION1 = '1ApWapzMBu8PQ-AH74JwzGiDk-8szOKAgE-gX9NikTKSRXwY-MQzXAHZ53UWPmcJL51fJ9nOqaVhDikTfmGaHH7wFiyXiyu1jcBV-rTd3yjpblZl5mAy5cSqnNzJ7W50FpC7pEX95sf0gZp664G5mvGMXaJwdzPP4JjWlz7vBRqcsoy_fs_aP2iQKYSoe-vz1fPQodrzLHK9bz-3Ll00Rc4nYncesTTSXUqp7jTbXoLoGYYyRdLF0LbJpvKhl6hnaoa-Ne1QFCoCCAY-rDo2uox2iMYb9Js72XOaG2I72y1G-tozPkg9I8jy2dLMv_mvOtLg3nIas9FL-fo4czEEGaFQ2Ql00BGM='

API_ID=23473442
API_HASH='0cd1d983e8b65e8d992b3b756f9a8eb1'
SESSION = '1ApWapzMBu5dktGQ43RS84-w5FU9SSxYTaD5AToAWNmGPWK5VajyQ4kaMwhmIxffbul4WptG6WehaW9aizuj_D-zoUVEwKaxNQqdnQm2XY5ei8MtaPrRcJD5LDpWK4xsL-njOWKM6EJ4yEl4y7d-RIXPG9FiBNv4KtShPDtwDGbaf9IVHR1vyPiaKyLS7qykHXyojvvUB3_pjbwbQaNOS4FWF0eD8XMm_TWG4thr2kUUrQPtPhTYA_IvZU78KeonG8AF-uMCuAhulI80EBqMvtHS5geR_by4Su5t8BeaTeBEdCTieEkkiVrEOp8fB49e2Nzy3u-XI4H1ORwOcSpCq6s-5iH_zNJA='

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
