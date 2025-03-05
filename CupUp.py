import asyncio
import json
import requests
from requests import request
import datetime

from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

BOT_TOKEN = '7796959944:AAEQsNrIdiFJJcesMkF-IuerzzaRex5bGwo'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
BASE_URL = "https://cuplegend.ru"
time = datetime.datetime.now()
step = 0

def time1():
    global time
    return((datetime.datetime.now()-time).total_seconds())

def step1():
    global step
    return(step)

async def limit(method, url):
    global time, step
    dtime = (datetime.datetime.now()-time).total_seconds()
    while step <= 100:
        if dtime > 1:
            if method==None:
                print(datetime.datetime.now())
                step = 1
                time = datetime.datetime.now()
                result=requests.get(url)
                return(result)
            else:
                print(datetime.datetime.now())
                step = 1
                time = datetime.datetime.now()
                result = request(method=method, url=url)
                return(result)
        elif step ==1:
            if method==None:
                print(datetime.datetime.now())
                step = step+1
                result=requests.get(url)
                return(result)
            else:
                print(datetime.datetime.now())
                step = step+1
                result = request(method=method, url=url)
                return(result)
        else:
            dtime = time1()
            step = step1()


async def get_stats():
    try:
        await asyncio.sleep(0.25)
        response = await limit(method="GET", url=f"{BASE_URL}/stats")
        response.raise_for_status()

        result = response.json()
        if response.status_code == 200:
            return result["players"]
        else:
             print(f"Ошибка при получении никнейма для UUID:. Статус код: {response.status_code}.  Ответ: {response.text}")
             return None
    except requests.exceptions.RequestException as e:
        print(f"Ошибка сети при запросе к API для UUID. Ошибка: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON при получении никнейма для UUID. Ошибка: {e}. Ответ: {response.text if 'response' in locals() else 'Ответ не получен'}")
        return None
    except Exception as e:
        print(f"Неизвестная ошибка при получении никнейма для UUID: Ошибка: {e}")
        return None


async def get_nickname_by_uuid(uuid):
    try:
        await asyncio.sleep(0.25)
        response = await limit(method="GET", url=f"{BASE_URL}/account/{uuid}")
        response.raise_for_status()

        result = response.json()
        if response.status_code == 200:
            return result.get("nickname", None)
        else:
             print(f"Ошибка при получении никнейма для UUID: {uuid}. Статус код: {response.status_code}.  Ответ: {response.text}")
             return None
    except requests.exceptions.RequestException as e:
        print(f"Ошибка сети при запросе к API для UUID: {uuid}. Ошибка: {e}")
        return "скрыт"
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON при получении никнейма для UUID: {uuid}. Ошибка: {e}. Ответ: {response.text if 'response' in locals() else 'Ответ не получен'}")
        return None
    except Exception as e:
        print(f"Неизвестная ошибка при получении никнейма для UUID: {uuid}. Ошибка: {e}")
        return "скрыт"

async def clan_nick(uuid):
    try:
        await asyncio.sleep(0.25)
        response = await limit(method="GET", url=f"{BASE_URL}/clan/{uuid}")
        response.raise_for_status()

        result = response.json()
        if response.status_code == 200:
            return result["name"]
        else:
             print(f"Ошибка при получении никнейма для UUID: {uuid}. Статус код: {response.status_code}.  Ответ: {response.text}")
             return None
    except requests.exceptions.RequestException as e:
        print(f"Ошибка сети при запросе к API для UUID: {uuid}. Ошибка: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON при получении никнейма для UUID: {uuid}. Ошибка: {e}. Ответ: {response.text if 'response' in locals() else 'Ответ не получен'}")
        return None
    except Exception as e:
        print(f"Неизвестная ошибка при получении никнейма для UUID: {uuid}. Ошибка: {e}")
        return None

async def get_starbox_info(ubid):
    """Получает информацию о StarBox по UBID."""
    try:
        await asyncio.sleep(0.25)
        response = await limit(None, f"{BASE_URL}/sb/{ubid}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении информации о боксе {ubid}: {e}")
        return "api_error"
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON при получении информации о боксе {ubid}: {e}")
        return None

async def get_player_info(uuid):
    """Получает информацию об игроке по UUID."""
    try:
        await asyncio.sleep(0.25)
        response = await limit(None, f"{BASE_URL}/account/{uuid}")
        response.raise_for_status()
        player_data = response.json()
        return player_data
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении информации об игроке {uuid}: {e}")
        if 'response' in locals() and hasattr(response, 'status_code') and response.status_code == 404:
            try:
                error_data = response.json()
                if error_data.get("msg") == "Пользователь скрыл свой аккаунт":
                    return "player_not_found"
                if error_data.get("msg") == "Превышен лимит запросов в секунду с одного IP-адреса":
                    return "лимит"
                if error_data.get("msg") == "Аккаунта с указанным UUID не существует":
                    return "несуществует"
            except json.JSONDecodeError:
                print("Не удалось декодировать JSON в блоке RequestException")
                return "api_error"
        return "api_error"
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON при получении информации о игроке {uuid}: {e}")
        return None
    except Exception as e:
        print(f"Неизвестная ошибка при получении информации об игроке {uuid}: {e}")
        return None

async def clan_info(uuid):
    try:
        await asyncio.sleep(0.25)
        response = await limit(None, f"{BASE_URL}/clan/{uuid}")
        response.raise_for_status()
        player_data = response.json()
        return player_data
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении информации об игроке {uuid}: {e}")
        if 'response' in locals() and hasattr(response, 'status_code') and response.status_code == 404:
            try:
                error_data = response.json()
                if error_data.get("msg") == "Превышен лимит запросов в секунду с одного IP-адреса":
                    return "лимит"
                if error_data.get("msg") == "Клана с указанным UCID не существует":
                    return "несуществует"
            except json.JSONDecodeError:
                print("Не удалось декодировать JSON в блоке RequestException")
                return "api_error"
        return "api_error"
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON при получении информации о игроке {uuid}: {e}")
        return None
    except Exception as e:
        print(f"Неизвестная ошибка при получении информации об игроке {uuid}: {e}")
        return None

async def pet_info(uuid):
    try:
        await asyncio.sleep(0.25)
        response = await limit(None, f"{BASE_URL}/hero/{uuid}")
        response.raise_for_status()
        player_data = response.json()
        return player_data
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении информации об игроке {uuid}: {e}")
        if 'response' in locals() and hasattr(response, 'status_code') and response.status_code == 404:
            try:
                error_data = response.json()
                if error_data.get("msg") == "Превышен лимит запросов в секунду с одного IP-адреса":
                    return "лимит"
                if error_data.get("msg") == "Персонажа с указанным UHID не существует":
                    return "несуществует"
            except json.JSONDecodeError:
                print("Не удалось декодировать JSON в блоке RequestException")
                return "api_error"
        return "api_error"
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON при получении информации о игроке {uuid}: {e}")
        return None
    except Exception as e:
        print(f"Неизвестная ошибка при получении информации об игроке {uuid}: {e}")
        return None

async def get_gift_info(ugid):
    """Получает информацию о подарке по UGID."""
    try:
        await asyncio.sleep(0.25)
        url = f"{BASE_URL}/gift/{ugid}"
        response = await limit(None, url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении информации о подарке {ugid}: {e}")
        return "api_error" 
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON при получении информации о подарке {ugid}: {e}")
        return None
async def clean_value(value):
    if value in (0, '-', None, [], "Player"):
        return None
    return value


@dp.inline_query()
async def inline_callback(inline: types.InlineQuery):
    query_text = inline.query
    results = []
    if inline.query == "channel":
        markup = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text='Меню', switch_inline_query="")]])
    else:
        markup = InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text='Меню', switch_inline_query_current_chat="")]])
    if not query_text:
        results.append(
            types.InlineQueryResultArticle(
                id="player_info_request",
                title="👤 Информация о игроке 👤",
                description="Введите UUID игрока",
                reply_markup=markup,
                input_message_content=types.InputTextMessageContent(
                    message_text="<b>⚠️ Введите UUID игрока ⚠️</b>", parse_mode='HTML'
                )
            )
        )
        results.append(
            types.InlineQueryResultArticle(
                id="pet_info_request",
                title="🐹 Информация о персонаже 🐹",
                description="Введите UHID персонажа",
                reply_markup=markup,
                input_message_content=types.InputTextMessageContent(
                    message_text="<b>⚠️ Введите UHID персонажа ⚠️</b>", parse_mode='HTML'
                )
            )
        )
        results.append(
            types.InlineQueryResultArticle(
                id="clan_info_request",
                title="🛡 Информация о клане 🛡",
                description="Введите UCID клана",
                reply_markup=markup,
                input_message_content=types.InputTextMessageContent(
                    message_text="<b>⚠️ Введите UCID клана ⚠️</b>", parse_mode='HTML'
                )
            )
        )
        results.append(
            types.InlineQueryResultArticle(
                id="gift_info_request",
                title="🎁 Информация о подарке 🎁",
                description="Введите UGID подарка",
                reply_markup=markup,
                input_message_content=types.InputTextMessageContent(
                    message_text="<b>⚠️ Введите UGID подарка ⚠️</b>", parse_mode='HTML'
                )
            )
        )
        results.append(
            types.InlineQueryResultArticle(
                id="box_info_request",
                title="📦 Информация о боксе 📦",
                description="Введите UBID бокса",
                reply_markup=markup,
                input_message_content=types.InputTextMessageContent(
                    message_text="<b>⚠️ Введите UBID бокса ⚠️</b>", parse_mode='HTML'
                )
            )
        )
    elif query_text.isdigit():
        search_id = query_text
        results.append(
            types.InlineQueryResultArticle(
                id=f"player_info_{search_id}",
                title=f"👤 Игрок c UUID » {search_id} 👤",
                input_message_content=types.InputTextMessageContent(
                    message_text=f"<b><i>🔎 Ищу игрока с UUID » {search_id}...</i></b>", parse_mode='html'
                ),
                description=f"Информация о игроке » {search_id}",
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(
                                text="...",
                                callback_data=f"пп"
                            )
                        ]
                    ]
                )
            )
        )
        results.append(
            types.InlineQueryResultArticle(
                id=f"pet_info_{search_id}",
                title=f"🐹 Персонаж c UHID » {search_id} 🐹",
                input_message_content=types.InputTextMessageContent(
                    message_text=f"<b><i>🔎 Ищу персонажа с UHID » {search_id}...</i></b>", parse_mode='html'
                ),
                description=f"Информация о персонаже » {search_id}",
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(
                                text="...",
                                callback_data=f"ппп"
                            )
                        ]
                    ]
                )
            )
        )
        results.append(
            types.InlineQueryResultArticle(
                id=f"clan_info_{search_id}",
                title=f"🛡 Клан c UCID » {search_id} 🛡",
                input_message_content=types.InputTextMessageContent(
                    message_text=f"<b><i>🔎 Ищу клан с UCID » {search_id}...</i></b>", parse_mode='html'
                ),
                description=f"Информация о клане » {search_id}",
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(
                                text="...",
                                callback_data=f"ппп"
                            )
                        ]
                    ]
                )
            )
        )
        results.append(
            types.InlineQueryResultArticle(
                id=f"gift_info_{search_id}",
                title=f"🎁 Подарок #{search_id} 🎁",
                input_message_content=types.InputTextMessageContent(
                    message_text=f"<b>🔎 Ищу подарок #{search_id}...</b>", parse_mode='html'
                ),
                description=f"Информация о подарке #{search_id}",
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(
                                text="...",
                                callback_data=f"пп"
                            )
                        ]
                    ]
                )

            )
        )
        results.append(
            types.InlineQueryResultArticle(
                id=f"box_info_{search_id}",
                title=f"📦 Бокс #{search_id} 📦",
                input_message_content=types.InputTextMessageContent(
                    message_text=f"<b><i>🔎 Ищу бокс #{search_id}...</i></b>", parse_mode='html'
                ),
                description=f"Информация о боксе #{search_id}",
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(
                                text="...",
                                callback_data=f"пп"
                            )
                        ]
                    ]
                )
            )
        )
    else:
        results.append(
            types.InlineQueryResultArticle(
                id="invalid_query",
                title="Некорректный запрос",
                description="Пожалуйста, введите числовой UGID.",
                reply_markup=markup,
                input_message_content=types.InputTextMessageContent(
                    message_text="Пожалуйста, введите числовой UGID."
                )
            )
        )

    await inline.answer(
        results=results,
        cache_time=1,
    )




@dp.chosen_inline_result()
async def chosen(inline: types.ChosenInlineResult):
    chosen_id = inline.result_id
    search_id = inline.query
    if chosen_id.startswith("box_info_request"):
        return
    if chosen_id.startswith("gift_info_request"):
        return
    if chosen_id.startswith("player_info_request"):
        return
    if chosen_id.startswith("pet_info_request"):
        return
    if chosen_id.startswith("clan_info_request"):
        return
    if chosen_id.startswith("gift_info_"):
        await process_gift_info(inline, search_id)
    if chosen_id.startswith("box_info_"):
        await process_box_info(inline, search_id)
    if chosen_id.startswith("player_info_"):
        await process_player_info(inline, search_id)
    if chosen_id.startswith("pet_info_"):
        await process_pet_info(inline, search_id)
    if chosen_id.startswith("clan_info_"):
        await process_clan_info(inline, search_id)

def форматировать_трофеи(трофеи):
  if isinstance(трофеи, int):
    return "{:,}".format(трофеи).replace(",", ",")
  else:
    return трофеи

async def process_clan_info(inline: types.ChosenInlineResult, uuid_str: str):
    if inline.query == "channel":
        markup = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text='Меню', switch_inline_query="")]])
    else:
        markup = InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text='Меню', switch_inline_query_current_chat="")]])

    clan = await clan_info(uuid_str)

    if clan == "несуществует":
        await bot.edit_message_text(inline_message_id=inline.inline_message_id,
                                    text=f"<b>⚠️ Клана с UCID » <code>{uuid_str}</code> не существует ⚠️</b>",
                                    parse_mode="HTML", reply_markup=markup)
        return
    if clan == "лимит":
        await bot.edit_message_text(inline_message_id=inline.inline_message_id,
                                    text=f"<b>💠 Превышен лимит запросов к API 💠</b>",
                                    parse_mode="HTML", reply_markup=markup)
        return
    a1 = clan["name"]
    a2 = clan["leader"]
    a3 = clan["level"]
    a4 = clan["create_date"]["date"]
    a5 = clan["create_date"]["time"]
    a6 = clan["description"]
    a7 = clan["rating"]
    a8 = clan["members"]
    a9 = await get_nickname_by_uuid(a2)
    if a9 == "скрыт":
        a2 = "скрыт"
    else:
        a2 = f"<a href='t.me/CupLegendBot?start=Account={a2}'>{await get_nickname_by_uuid(a2)}</a>"
    member_list = []
    for member_uuid, member_data in a8.items():
        date_str = member_data["date"]
        time_str = member_data["time"]
        datetime_str = f"{date_str} {time_str}"
        try:
            join_datetime = datetime.datetime.strptime(datetime_str, "%d.%m.%Y %H:%M:%S")
            member_list.append((member_uuid, member_data, join_datetime))
        except ValueError:
            print(f"Ошибка при разборе даты/времени: {datetime_str}")
            continue 
    member_list.sort(key=lambda item: item[2])

    async def get_member_info(member_uuid, member_data, index):
        nickname = await get_nickname_by_uuid(member_uuid)
        join_date = member_data["date"]
        join_time = member_data["time"]
        member_link = f"<a href='t.me/CupLegendBot?start=Account={member_uuid}'>{nickname}</a>"
        return f"👤 Участник #{index+1} » {member_link}\n  ⤷ Вступил » <code>{join_date}</code> в <code>{join_time}</code>\n"

    tasks = [get_member_info(uuid, data, i) for i, (uuid, data, _) in enumerate(member_list)]
    member_strings = await asyncio.gather(*tasks)
    members_string = "".join(member_strings)
    await bot.edit_message_text(inline_message_id=inline.inline_message_id, text=f"<b>🛡 Информация о клане с UCID » {uuid_str} ⤸\n\n<blockquote>🏷 Название » <a href='t.me/CupLegendBot?start=ClanInfo={uuid_str}'>{a1}</a>\n  ⤷ 📚 Уровень » <code>{a3}</code>\n  ⤷ 🔱 Рейтинг » <code>{a7}</code>\n\n📅 Создан » <code>{a4}</code> в <code>{a5}</code>\n  ⤷ 👑 Лидер » {a2}\n\n📝 Описание ⤸\n\n{a6}</blockquote>\n\n👤 Участники ⤸\n<blockquote expandable>{members_string}</blockquote>\n🔍 Найти информацию о клане можно нажав на кнопку ниже:</b>", parse_mode="HTML", disable_web_page_preview=True, reply_markup=markup)

async def process_pet_info(inline: types.ChosenInlineResult, uuid_str: str):
    if inline.query == "channel":
        markup = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text='Меню', switch_inline_query="")]])
    else:
        markup = InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text='Меню', switch_inline_query_current_chat="")]])

    pet = await pet_info(uuid_str)

    if pet == "несуществует":
        await bot.edit_message_text(inline_message_id=inline.inline_message_id,
                                    text=f"<b>⚠️ Персонажа с UHID » <code>{uuid_str}</code> не существует ⚠️</b>",
                                    parse_mode="HTML", reply_markup=markup)
        return
    if pet == "лимит":
        await bot.edit_message_text(inline_message_id=inline.inline_message_id,
                                    text=f"<b>💠 Превышен лимит запросов к API 💠</b>",
                                    parse_mode="HTML", reply_markup=markup)
        return
    a1 = pet["creator"]
    a2 = pet["name"]
    a3 = pet["description"]
    a4 = pet["religion"]
    a5 = форматировать_трофеи(pet["wins"])
    a6 = форматировать_трофеи(pet["loses"])
    a7 = pet["level"]
    a8 = форматировать_трофеи(pet["trophies"])
    a9 = pet["create_date"]["date"]
    a10 = pet["create_date"]["time"]
    if await get_nickname_by_uuid(a1) == "скрыт":
        a1 = "скрыт"
    else:        
        a1 = f"<a href='t.me/CupLegendBot?start=Account={a1}'>{await get_nickname_by_uuid(a1)}</a>"
    await bot.edit_message_text(inline_message_id=inline.inline_message_id, text=f"<b>👾 Информация о персонаже с UHID » {uuid_str} ⤸\n\n<blockquote>🏷 Имя » «<a href='t.me/CupLegendBot?start=Hero={uuid_str}'>{a2}</a>»\n  ⤷ 📚 Уровень » <code>{a7}</code>\n   ⤷ 🕯 Сторона » <a href='t.me/CupLegendBot?start=Religions'>{a4}</a>\n\n🏆 Трофеи » <code>{a8}</code>\n  ⤷ 🟢 Победы » <code>{a5}</code>\n  ⤷ 🔴 Поражения » <code>{a6}</code>\n\n📅 Создан » <code>{a9}</code> в <code>{a10}</code>\n  ⤷ 👤 Создатель » {a1}\n\n📝 Описание ⤸\n\n{a3}</blockquote>\n\n🔍 Найти информацию о персонаже можно нажав на кнопку ниже:</b>", parse_mode="HTML", disable_web_page_preview=True, reply_markup=markup)


async def process_player_info(inline: types.ChosenInlineResult, uuid_str: str):
    if inline.query == "channel":
        markup = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text='Меню', switch_inline_query="")]])
    else:
        markup = InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text='Меню', switch_inline_query_current_chat="")]])

    player = await get_player_info(uuid_str)

    if player == "несуществует":
        await bot.edit_message_text(inline_message_id=inline.inline_message_id,
                                    text=f"<b>⚠️ Игрока с UUID » <code>{uuid_str}</code> не существует, так как всего игроков <code>{await get_stats()}</code>⚠️</b>",
                                    parse_mode="HTML", reply_markup=markup)
        return
    if player == "player_not_found":
        await bot.edit_message_text(inline_message_id=inline.inline_message_id,
                                    text=f"<b>👁 Игрок скрыл свой профиль 👁</b>",
                                    parse_mode="HTML", reply_markup=markup)
        return
    if player == "лимит":
        await bot.edit_message_text(inline_message_id=inline.inline_message_id,
                                    text=f"<b>💠 Превышен лимит запросов к API 💠</b>",
                                    parse_mode="HTML", reply_markup=markup)
        return

    s1 = player["nickname"]
    s2 = player["privilege"]
    s3 = player["level"]
    s4 = форматировать_трофеи(player["trophies"])
    s7 = player["clan"]
    t1 = player["reg_date"]["date"]
    t2 = player["reg_date"]["time"]
    t3 = player["online"]["date"]
    t4 = player["online"]["time"]
    if s7 == 0:
        s7 = "отсутствует"
    else:
        s7 = f"<a href='t.me/CupLegendBot?start=ClanInfo={s7}'>{await clan_nick(s7)}</a>"
    if s2 == "Legend":
        s2 = "<a href='t.me/CupLegendBot?start=Legend'>Legend</a>"
    if s2 == "Star":
        s2 = "<a href='t.me/CupLegendBot?start=Star'>Star</a>"
    else:
        s2 = s2
    await bot.edit_message_text(inline_message_id=inline.inline_message_id, text=f"<b>👤 Информация о игроке с UUID » {uuid_str} ⤸\n\n<blockquote>🏷 Никнейм » <a href='t.me/CupLegendBot?start=Account={uuid_str}'>{s1}</a>\n  ⤷ 🧬 Привилегия » {s2}\n   ⤷ 📚 Уровень » <code>{s3}</code>\n    ⤷ 🏆 Трофеи » <code>{s4}</code>\n\n🛡 Клан » {s7}\n\n📅 Регистрация » <code>{t1}</code> в <code>{t2}</code>\n  ⤷ 👁‍🗨 Онлайн » <code>{t3}</code> в <code>{t4}</code></blockquote>\n\n🔍 Найти информацию о игроке можно нажав на кнопку ниже:</b>", parse_mode="HTML", disable_web_page_preview=True, reply_markup=markup)


async def process_gift_info(inline: types.ChosenInlineResult, ugid_str: str):
    """Обрабатывает информацию о подарке."""
    gift_data = await get_gift_info(ugid_str)
    if inline.query == "channel":
        markup = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text='Меню', switch_inline_query="")]])
    else:
        markup = InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text='Меню', switch_inline_query_current_chat="")]])
    if gift_data == "api_error":
        await bot.edit_message_text(inline_message_id=inline.inline_message_id,
                                    text=f"<b>⚠️ Подарка #{ugid_str} не существует ⚠️</b>",
                                    parse_mode="HTML", reply_markup=markup)
        return

    if gift_data is None or "status_code" not in gift_data:
        await bot.edit_message_text(inline_message_id=inline.inline_message_id,
                                    text="<b>⚠️ Подарок с таким UGID не существует ⚠️</b>",
                                    parse_mode="HTML", reply_markup=markup)
        return

    gift = gift_data
    if gift["status_code"] == 200:
        meta = gift["meta"]
        sender_uuid = gift["sender"]
        sender_nickname = await get_nickname_by_uuid(sender_uuid)
        sender = "анонимно" if sender_uuid == 0 else f"<a href='t.me/CupLegendBot?start=Account={sender_uuid}'>{sender_nickname}</a>" if sender_uuid != "N/A" and sender_nickname else "N/A"
        received = gift["received"]
        rare = gift["meta"]["rare"]
        if rare == "Редкий":
            rare = "  ⤷ 🟣 Редкость » редкий"
        if rare == "Обычный":
            rare = "  ⤷ 🔵 Редкость » обычный"
        if "model" in gift and gift["model"]:
            model_data = gift["model"]
            if "upgraded" in model_data and model_data["upgraded"]:
                t1 = model_data["upgraded"]["date"]
                t2 = model_data["upgraded"]["time"]
            number = model_data.get("number", "N/A")
            gift_link = model_data.get("gift_link", "N/A")
            names = model_data.get("name", "N/A")
            chance = model_data.get("chance", "N/A")
        else:
            t1 = "N/A"
            t2 = "N/A"
            number = "-"
            gift_link = "-"
            names = "-"
            chance = "-"
        if t1 and t2 == "N/A":
            soo = f"  ⤷ Улучшен » <code>-</code>"
        else:
            soo = f"  ⤷ Улучшен » <code>{t1}</code> в <code>{t2}</code>"
        if chance == "-":
            chance = ""
        else:
            chance = f"({chance}%)"
        if names and chance == "-":
            s1 = ""
        else:
            s1 = f"  ⤷ Модель » {names} {chance}"
        if number == "-":
            number = f"{ugid_str}"
        link = meta.get("link", "N/A") if isinstance(meta, dict) else "N/A"
        name = meta.get("name", "N/A") if isinstance(meta, dict) else "N/A"
        ticker = meta["ticker"] if isinstance(meta, dict) else "N/A"
        received_date = received.get("date", "N/A") if isinstance(received, dict) else "N/A"
        received_time = received.get("time", "N/A") if isinstance(received, dict) else "N/A"
        received_formatted = f"<code>{received_date}</code> в <code>{received_time}</code>" if received_date != "N/A" and received_time != "N/A" else "N/A"
        owner_uuid = gift["owner"]
        owner_nickname = await get_nickname_by_uuid(owner_uuid)
        owner = "скрыт" if owner_uuid == 0 else "подарок сожжён" if owner_uuid == -1 else f"<a href='t.me/CupLegendBot?start=Account={owner_uuid}'>{owner_nickname}</a>" if owner_uuid != "-" and owner_nickname else "-"
        links = f"<a href='{gift_link}'>перейти</a>"
        show_number = f"{ticker} <a href='{link}'>{name}</a> #{number}"
        if owner_uuid == -1:
            show_number = f"{ticker} <a href='{link}'>{name}</a> #{ugid_str}"
            links = "-"

        await bot.edit_message_text(inline_message_id=inline.inline_message_id,text=f"<b>🎁 Информация о подарке #{ugid_str} ⤸\n\n<blockquote>{show_number}\n{s1}\n{rare}\n\n👤 Владелец » {owner}\n{soo}\n\n👤 Даритель » {sender}\n  ⤷ Дата отправки » {received_formatted}\n\n🔗 Ссылка на подарок » {links}</blockquote>\n\n🔍 Найти подарок можно нажав на кнопку ниже:</b>", parse_mode="HTML", disable_web_page_preview=True, reply_markup=markup)



async def process_box_info(inline: types.ChosenInlineResult, ubid_str: str):
    """Обрабатывает информацию о боксе."""
    star = await get_starbox_info(ubid_str)
    if inline.query == "channel":
        markup = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text='Меню', switch_inline_query="")]])
    else:
        markup = InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text='Меню', switch_inline_query_current_chat="")]])
    if star == "api_error":
        await bot.edit_message_text(inline_message_id=inline.inline_message_id,
                                    text=f"<b>⚠️ Бокса #{ubid_str} не существует ⚠️</b>",
                                    parse_mode="HTML", reply_markup=markup)
        return

    if star is None:
        await bot.edit_message_text(inline_message_id=inline.inline_message_id,
                                    text="<b>⚠️ Бокс с таким UBID не существует ⚠️</b>",
                                    parse_mode="HTML", reply_markup=markup)
        return

    opener_uuid = star.get("opener", "N/A")
    opener_nickname = await get_nickname_by_uuid(opener_uuid)
    opener = "N/A" if opener_uuid == "N/A" else f"<a href='t.me/CupLegendBot?start=Account={opener_uuid}'>{opener_nickname}</a>" if opener_nickname else "N/A"
    rare = star["rare"]
    date = star["date"]
    meta = star["meta"]
    if rare == "обычный":
        rare = "<a href='t.me/CupLegendBot?start=SBInfo=default'>обычный</a>"
    if rare == "космический":
        rare = "<a href='t.me/CupLegendBot?start=SBInfo=space'>космический</a>"
    if rare == "легендарный":
        rare = "<a href='t.me/CupLegendBot?start=SBInfo=legend'>легендарный</a>"

    a1 = await clean_value(star["meta"].get("experience"))
    a2 = await clean_value(star["meta"].get("gems"))
    a3 = await clean_value(star["meta"].get("trophies"))
    a4 = await clean_value(star["meta"].get("tokens"))
    a5 = await clean_value(star["meta"].get("fragments"))
    a6 = await clean_value(star["meta"].get("energy"))
    a7 = await clean_value(star["meta"].get("privilege"))
    a8 = await clean_value(star["meta"].get("rune"))
    a9 = await clean_value(star["meta"].get("artifact"))
    a10 = star["meta"].get("weapons")
    t1 = star["date"]["date"]
    t2 = star["date"]["time"]
    if inline.query == "channel":
        markup = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text='Меню', switch_inline_query="")]])
    else:
        markup = InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text='Меню', switch_inline_query_current_chat="")]])

    rewards = []
    if a1 is not None:
        rewards.append(f"• Опыт » <code>{a1}</code>")
    if a2 is not None:
        rewards.append(f"• Гемы » <code>{a2}</code>")
    if a3 is not None:
        rewards.append(f"• Трофеи » <code>{a3}</code>")
    if a4 is not None:
        rewards.append(f"• CLTokens » <code>{a4}</code>")
    if a5 is not None:
        rewards.append(f"• Фрагменты » <code>{a5}</code>")
    if a6 is not None:
        rewards.append(f"• Энергия » <code>{a6}</code>")
    if a7 is not None:
        rewards.append(f"• Привилегия » <code>{a7}</code>")
    if a8 is not None:
        rewards.append(f"• Руна » <code>{a8}</code>")
    if a9 is not None:
        rewards.append(f"• Артефакт » <code>{a9}</code>")
    if a10:
        if isinstance(a10, list) and len(a10) > 0:
            weapons_str = a10[0]
            rewards.append(f"• Оружие » <code>{weapons_str}</code>")


    rewards_text = "\n".join(rewards)
    await bot.edit_message_text(inline_message_id=inline.inline_message_id, text=f"<b>📦 Информация о <a href='t.me/CupLegendBot?start=SBView={ubid_str}'>StarBox #{ubid_str}</a> ⤸\n\n<blockquote>👤 Открыл » {opener}\n  ⤷ Редкость » {rare}\n  ⤷ Дата » <code>{t1}</code> в <code>{t2}</code>\n\n💎 Награды ⤸\n\n{rewards_text}</blockquote>\n\n🔍 Найти бокс можно нажав на кнопку ниже:</b>", parse_mode="HTML", disable_web_page_preview=True, reply_markup=markup)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
