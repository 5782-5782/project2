import asyncio
import logging
import sqlite3

from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.types import Message, InlineKeyboardButton, WebAppInfo, CallbackQuery, ChosenInlineResult
from aiogram.utils.keyboard import InlineKeyboardBuilder

logging.basicConfig(level=logging.INFO)
BOT_TOKEN = '7775440771:AAFLb1IJg1gOoQmnhNosUKkvg0eG_VC_YPg'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

connection = sqlite3.connect("RP.db")
cursor = connection.cursor()
cursor.execute(
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
    id = cursor.execute("SELECT id FROM msg ORDER BY id DESC LIMIT 1").fetchall()
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
        cursor.execute("INSERT INTO msg (username, text, sender) VALUES (?, ?, ?)", (username, text1, f"@{inline.from_user.username}",))
        connection.commit()
        msg_id = inline.inline_message_id
        print(msg_id)
        await bot.edit_message_text(text=f"Это сообщение может прочитать только {username}", inline_message_id=msg_id)
        await bot.edit_message_reply_markup(reply_markup=InlineKeyboardBuilder().add(InlineKeyboardButton(text="_Прочитать сообщение_", callback_data=db())).as_markup(), inline_message_id=msg_id)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
