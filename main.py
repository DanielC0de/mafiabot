from datetime import datetime, timedelta
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import chat_permissions, ChatType
from config import TOKEN
import os
from random import choice
from asyncio import sleep
from aiogram.dispatcher import filters

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

all_roles = os.listdir("/home/daniel41k/programming/python/bots/mafia/roles")
ROLES = []
@dp.message_handler(commands=["start"])
async def mafia(message: types.Message):
    await message.answer("Привет, я бот для игры в мафию. С помощью меня ты можешь поиграть в эту невероятную игру, для этого тебе просто нужно ввести команду \"/game\" без кавычек.")
    await sleep(10)
    await message.answer("""Так же ты можешь ввести дополнительные параметры:
\"/game -маньяк\" - уберет из игры маньяка, по умолчанию он есть. Важно вводить первым значением после /game.
\"/game число\" - количество игроков в игре. Минимум 8. Важно вводить последним значением. <b>Важно, вводите число игроков, исключая ведущего.</b>
\"/game -маньяк 10\" - пример ввода.
""", parse_mode="HTML")
    

@dp.message_handler(commands=["play"])
async def mafia(message: types.Message):
    global ROLES, all_roles
    ROLES = all_roles
    msg = message.text.replace("/play", "").split()
    if len(msg) > 0:
        if msg[0] == "-маньяк":
            if msg[-1] != "12":
                ROLES.remove("maniac.jpg")
                ROLES.append("maf.jpg")
            else: 
                message.answer("Слишком много мафий, вы так не думаете?")
        if msg[-1] == "9":
            ROLES.append("mir.jpg")
        elif msg[-1] == "10":
            ROLES.append("mir.jpg")
            ROLES.append("maf.jpg")
        elif msg[-1] == "11":
            ROLES.append("mir.jpg")
            ROLES.append("mir.jpg")
            ROLES.append("maf.jpg")
        elif msg[-1] == "12":
            ROLES.append("mir.jpg")
            ROLES.append("mir.jpg")
            ROLES.append("maf.jpg")
            ROLES.append("maf.jpg")
    for i in range(len(ROLES)):
        role = choice(ROLES)
        ROLES.remove(role)
        photo = open('/home/daniel41k/programming/python/bots/mafia/roles/' + role, 'rb')
        await message.answer(f"Игрок {i+1}:")
        await bot.send_photo(message.from_user.id, photo)
        await sleep(10)
    await message.answer("===========================================")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
