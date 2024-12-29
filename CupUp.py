import asyncio
import logging
import datetime
import random
import string
import aiogram

from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.types import Message, InlineKeyboardButton, WebAppInfo, CallbackQuery, ChosenInlineResult
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.client.bot import DefaultBotProperties

default=DefaultBotProperties(parse_mode='html')
logging.basicConfig(level=logging.INFO)
bot = Bot('7775440771:AAFLb1IJg1gOoQmnhNosUKkvg0eG_VC_YPg')
bot1 = Bot('7566430370:AAGMGbA7H0lE75PUCXnhIlr9QWGc5bQyxGg')
bot2 = Bot('7738138639:AAGRga5bEmp-Sj0qtMADJF97x0bBtTiEV9s')
bot3 = Bot('7885243241:AAHw6GlLRrizM5Jfxe9WTc_Vn3Bo152q_dI')
bot4 = Bot('7600361798:AAHk3i0NbPpDeYxe1q9oabmHfYAUGR8ocA4')
bot5 = Bot('7787661963:AAFUtALPbFZqIKCWvX5O_UqPlRIi2fLjfIw')
dp = Dispatcher()

iii = 0

@dp.message(F.text)
async def handle_rp_command(message: Message):

    global iii
    if "go party" in message.text and message.from_user.id == 1776244625 and message.chat.id == -1002445135554 and iii == 0:
        iii = 1
        await bot.promote_chat_member(-1002445135554, 7566430370, False, True, True, True, True, True, True, True, True, True, True, True, True, True)
        msg = await message.reply("Идёт подготовка 1/10")
        await asyncio.sleep(1)
        await bot.promote_chat_member(-1002445135554, 7738138639, False, True, True, True, True, True, True, True, True, True, True, True, True, True)
        await asyncio.sleep(1)
        await bot.promote_chat_member(-1002445135554, 7885243241, False, True, True, True, True, True, True, True, True, True, True, True, True, True)
        await msg.edit_text("Идёт подготовка 3/10")
        await asyncio.sleep(1)
        await bot.promote_chat_member(-1002445135554, 7600361798, False, True, True, True, True, True, True, True, True, True, True, True, True, True)
        await asyncio.sleep(1)
        await bot.promote_chat_member(-1002445135554, 7787661963, False, True, True, True, True, True, True, True, True, True, True, True, True, True)
        await msg.edit_text("Идёт подготовка 5/10")
        await asyncio.sleep(1)
        await bot.set_chat_administrator_custom_title(-1002445135554, 7566430370, "Подарок 1")
        await asyncio.sleep(1)
        await bot.set_chat_administrator_custom_title(-1002445135554, 7738138639, "Подарок 2")
        await msg.edit_text("Идёт подготовка 7/10")
        await asyncio.sleep(1)
        await bot.set_chat_administrator_custom_title(-1002445135554, 7885243241, "Подарок 3")
        await asyncio.sleep(1)
        await bot.set_chat_administrator_custom_title(-1002445135554, 7600361798, "Подарок 4")
        await asyncio.sleep(1)
        await bot.set_chat_administrator_custom_title(-1002445135554, 7787661963, "Подарок 5")
        await msg.edit_text("Подготовка окончена 10/10 следующая часть: поздравление.")
        await asyncio.sleep(5)
        await msg.delete()
        await bot1.send_message(-1002445135554, "Никому не двигаться! Работает омон под метр сорок пять! Лицами в пол!")
        await asyncio.sleep(1)
        await bot2.send_message(-1002445135554, "Нам нужен Глеф! Мы знаем, что он пытается скрыться! Отдайте его и никто не пострадает!")
        await asyncio.sleep(1)
        await bot3.send_message(-1002445135554, "Ну-ну, потише. Итак. Мы от сообщества карликов. Нам нужен Глеф. Он обвиняется в преступлениях против меньшинств! Угрозы физической расправой, через, цитирую: тюк кирпичиком по макушке. Неоднократные оскорбления карликового народа. Принижение маленьких достоинств. Безжалостный геноцид китов. И слом бижи нашего крало-брата Аяна! Но главное - это попытка покинуть Эпсу. Такое - не прощается!")
        await asyncio.sleep(60)
        await bot1.send_message(-1002445135554, "А ещё он великан! Чёртов великан метр восемьдесят! ")
        await asyncio.sleep(1)
        await bot2.send_message(-1002445135554, "Точно! На цепь его! И в намордник! Мутант-переросток! ")
        await bot3.send_message(-1002445135554, "Так что выдайте нам его немедленно. Пусть даже не надеется что лив из Эпсы его спасёт! Никто не покидает Эпсу так просто... Часть команды - часть корабля! Под вечным правлением величайшего из нижайших - Кельта! Мы посадим Глефа на цепь в подвале, и заставим вечно играть в Эпсилон вар и восхвалять в общаке разработчиков в целом и Кельта лично!")
        await asyncio.sleep(1)
        await bot1.send_message(-1002445135554, "И выстройтесь по росту! Всем, кто выше полутора метров мы отпилим ноги и примем в нашу общину! Быстрее, чёртовы гиганты!")
        await bot5.send_message(-1002445135554, "Споры, ругань, приход ежа")
        await asyncio.sleep(240)
        await bot3.send_message(-1002445135554, "Ага.. Значит не хотите по хорошему? Ну что же... Вы сами до этого довели!")
        await asyncio.sleep(1)
        await bot1.send_message(-1002445135554, "Нужно звать короля! Маленького гиганта!")
        await asyncio.sleep(1)
        await bot2.send_message(-1002445135554, "Да да! КЕЕЕЕЛЬТ!")
        await asyncio.sleep(1)
        await bot3.send_message(-1002445135554, "Мастер Кельт, придите! ")
        await asyncio.sleep(1)
        await bot1.send_message(-1002445135554, "Владыка карликовостиии!")
        await asyncio.sleep(1)
        await bot5.send_message(-1002445135554, "Приходит кельт...")
        await asyncio.sleep(1)
        await bot4.send_message(-1002445135554, "Так, что тут происходит?")
        await asyncio.sleep(1)
        await bot3.send_message(-1002445135554, "Здраствуйте ваше нижайшество! Треклятые великаны укрывают страшного преступника и отказываются от сотрудничества! Более того, этот... Глеф посмел желать лива без вашего дозволения!")
        await asyncio.sleep(1)
        await bot4.send_message(-1002445135554, "Что?! Ливать без бана?!")
        await asyncio.sleep(15)
        await bot1.send_message(-1002445135554, "Да-да! А все остальные, они прячут Глефа! А Глеф - преступник! Враг малого народа!")
        await asyncio.sleep(15)
        await bot4.send_message(-1002445135554, "Вот как. Неповиновение будет наказано! Лагами!")
        await asyncio.sleep(1)
        await bot2.send_message(-1002445135554, "Да! Лагов им! Пусть эпса лагает! ")
        await asyncio.sleep(3)
        await bot1.send_message(-1002445135554, "Так она уже лагает... Ивент же.")
        await asyncio.sleep(1)
        await bot3.send_message(-1002445135554, "Значит будет лагать ещё сильнее! Нет предела совершенству!")
        await asyncio.sleep(180)
        await bot4.send_message(-1002445135554, "Всё ещё держитесь? Какие упорные гиганты! Ну что же! Тогда... Получайте урезание дропа! на 30.. Нет! 50 процентов!")
        await asyncio.sleep(180)
        await bot3.send_message(-1002445135554, "Поняли что мы не шутим? Получайте карликовый дроп треклятые великаны!")
        await bot5.send_message(-1002445135554, "появление бурундука, ругань на отсутствие колец в данже")
        await asyncio.sleep(240)
        await bot4.send_message(-1002445135554, "Ну что сдаётесь? Нет...?! Тогда... Последний шаг! Вы сами меня вынудили! Всем баны! Всем кроме ГЛЕФА! Его в вечный фарм данжей... Сквозь лаги и без дропа!")
        await asyncio.sleep(1)
        await bot5.send_message(-1002445135554, "Хель...")
        await asyncio.sleep(60)
        await bot1.send_message(-1002445135554, "Что? Нейропесни? Нееееет! Наша единственная слабость! ")
        await asyncio.sleep(1)
        await bot2.send_message(-1002445135554, "Единственная кроме ударов пенисами по тыковкам! Нииииии!")
        await asyncio.sleep(1)
        await bot3.send_message(-1002445135554, "Пожалуйста! Только не это!")
        await asyncio.sleep(1)
        await bot4.send_message(-1002445135554, "Мои карликовые уши! Они оскорблены! Нееет! Бегите! спасайтесь пока мы ещё сильнее не уменьшились от песенки Хель!")
        await asyncio.sleep(1)
        await bot1.send_message(-1002445135554, "Я исчезаю! Я слишком маленький! Мои маленькие ножки не могут так быстро двигаться чтобы убежать!")
        await bot1.leave_chat(-1002445135554)
        await asyncio.sleep(1)
        await bot2.send_message(-1002445135554, "Каждый сам за себя!")
        await bot2.leave_chat(-1002445135554)
        await asyncio.sleep(1)
        await bot4.send_message(-1002445135554, "Вы выиграли битву... Но не войну! Мы вернёмся! И станем ещё меньше! С нами придёт Шахмотигр... знайте! Карлики победят!")
        await bot3.leave_chat(-1002445135554)
        await bot4.leave_chat(-1002445135554)
        await bot5.send_message(-1002445135554, "Created by @Mishi5782. \nAddressed to the @glefton. \n Have a nice holiday!")
        await bot5.leave_chat(-1002445135554)
        iii = 0



async def main():
    await dp.start_polling(bot, bot1, bot2, bot3, bot4, bot5)

if __name__ == "__main__":
    asyncio.run(main())
