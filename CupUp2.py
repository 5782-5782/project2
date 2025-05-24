import datetime
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
BOT_TOKEN = '8188395101:AAFm8J8eCQ-Fv1EKOLh1lzTKLEGxEv_Y2f0'

logging.basicConfig(level=logging.INFO)

CHANNEL_ID = -1002384182799

events = [
    {
        "name": "До нового года",
        "month": 1,
        "day": 1,
        "hour": 0,
        "minute": 0,
        "second": 0,
        "message_ids": [11]
    },
    {
        "name": "До зимы",
        "month": 12,
        "day": 1,
        "hour": 0,
        "minute": 0,
        "second": 0,
        "message_ids": [12]
    },
    {
        "name": "До лета",
        "month": 6,
        "day": 1,
        "hour": 0,
        "minute": 0,
        "second": 0,
        "message_ids": [13]
    },
    {
        "name": "До дня рождения миши (@Mishi5782)",
        "month": 6,
        "day": 14,
        "hour": 0,
        "minute": 0,
        "second": 0,
        "message_ids": [14]
    },
]

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def update_messages():
    """Обновляет сообщения в канале с информацией о времени до событий."""
    now = datetime.datetime.now()
    for event in events:
        event_datetime = datetime.datetime(now.year, event["month"], event["day"], event["hour"], event["minute"], event["second"])

        if event_datetime < now:
            event_datetime = event_datetime.replace(year=now.year + 1)

        time_to_event = event_datetime - now

        time_to_event_formatted = str(time_to_event).split(".")[0]  # Убираем миллисекунды

        for message_id in event["message_ids"]:
            try:
                await bot.edit_message_text(
                    chat_id=CHANNEL_ID,
                    message_id=message_id,
                    text=f"{event['name']}\n<blockquote>{time_to_event_formatted}</blockquote>", parse_mode='html'
                )
            except Exception as e:
                print(f"{datetime.datetime.now()} Ошибка при обновлении сообщения {message_id}: {e}")

async def scheduler():
    """Запускает функцию обновления сообщений каждую секунду."""
    print("Программа успешно запущена!")
    while True:
        await update_messages()
        await asyncio.sleep(60)

async def on_startup():
    """Функция, вызываемая при запуске бота."""
    await scheduler()

async def main():
    await on_startup()

if __name__ == "__main__":
    asyncio.run(main())
