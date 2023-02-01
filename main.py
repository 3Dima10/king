import logging
import ch
import txt
import random
from aiogram import Dispatcher, Bot, executor, types

logging.basicConfig(level=logging.INFO)
bot = Bot(token="5797482707:AAF4OtObtp7uNLxw4QUOfkdGtsO8qLT8ft0")
dp = Dispatcher(bot)


##################
# _____START_____#
##################
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    pol = open("start.jpg", "rb")
    await bot.send_photo(message.chat.id, pol)
    kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cl1 = types.KeyboardButton("Король Игрок 👑")
    cl2 = types.KeyboardButton("Король Бот 🤖")
    cl3 = types.KeyboardButton("Донат💰")
    kls.add(cl1, cl2, cl3)
    await bot.send_message(message.chat.id,
                           f"Добро пожаловать в наш скромный обитель господин <b>{message.from_user.first_name}</b>\n"
                           "Ваш скромный слуга поможет вам и вашей свите сыграть в увлекательною игру\n"
                           "<b>Для начала выберете один из предложенных режимов:</b>\n"
                           "<b>1.</b><i>Король Игрок</i> = Король выбирается среди игроков и именно игрок отдает приказы либо запрашивает помощи у Бота\n"
                           "<b>2.</b><i>Король Бот</i> = Король по умолчанию становиться Бот и именно бот назначает каму и какой приказ отдать \n"
                           '<b>Небольшая паскалка от разработчика для парочек если выбрать <i>"Король Бот 🤖"</i> и выбрать <i>"2"</i> то включиться режим 🔞 \n</b>'
                           "Ознакомица с правилами /rules \n"
                           "Помощь /help",
                           parse_mode="html",
                           reply_markup=kls)


#################
# _____HELP_____#
#################
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cln = types.KeyboardButton("⬅️Назад")
    kls.add(cln)
    await bot.send_message(message.chat.id, "<i>/start</i> - Запустить или перезапустить бота \n"
                                            "<i>/rules</i> - Ознакомица с правилами игры \n "
                                            "<b>Доброго вечером суток господа этот недостойный переводчик просит вас если вы заметете какие-то ошибки или если сей бот упадет сообщить в нашу <i><a href='https://t.me/Dolar3510'>службу поддержки</a></i>, также прошу вас относиться с пониманием данный проект ещё свежий поэтому возможны ошибки за ранее благодарю \n "
                                            "Ваш покорный слуга желает вам хорошо провести время за игрой ❤ </b>",
                           parse_mode="html",
                           reply_markup=kls)


##################
# _____RUSEL_____#
##################
@dp.message_handler(commands=['rules'])
async def rules(message: types.Message):
    kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cln = types.KeyboardButton("⬅️Назад")
    kls.add(cln)
    await bot.send_message(message.chat.id,
                           '<b>В игре один из игроков избирается Королём (ou-sama - по-японски "король"), и затем он придумывает смешные задания, которые должны исполнять другие игроки. Игроки выглядят глупо при этом, поэтому игра не рекомендуется трезвым и робким людям.\n'
                           '<i>Вот как в неё играть : </i> \n '
                           'Берут палочки для еды, по одной на каждого игрока. На одной из них пишут "👑", на остальных - номера от 1 и выше. \n '
                           'Затем кто-то один берёт в кулак палочки (так, чтобы надписи не было видно) , и все участники по очереди выбирают палочку, но никому не говорят выпавший номер. Удачливый парень (или девушка) , получивший палочку с надписью "👑", избирается Королём. \n '
                           'Далее Король придумывает задание и выбирает номер игрока, который должен выполнить это задание (но сам Король не знает, у кого какой номер).\n '
                           'Примеры заданий: "№1 должен поцеловать №5" или "№3 должен станцевать Макарену" «Всю работу за вас зделает бот о преподобный Король » Это неизбежно приводит к неловким ситуациям. \n'
                           'После того, как все выполняют то, что должны; палочки собираются, и процесс повторяется.\n'
                           'Обычно у каждого есть шанс стать Королём, и игроки получают удовольствие от шанса отомстить тем, кто мучил их в предыдущих раундах игры.\n '
                           'Чем долше игра..., тем более жестокими становятся задания.\n'
                           '<i>И самое главное правило что желание короля не абсолютны и беспрекословны их нельзя изменить или отказаться выполнять поэтому играйте акуратно 😉 </i></b>\n'
                           '<b>Небольшая паскалка от разработчика для парочек если выбрать <i>"Король Бот 🤖"</i> и выбрать <i>"2"</i> то включиться режим 🔞 \n</b>'
                           '<i>PS:Вместо палочек можно взять карты одной масти перетасовать и раздать и тот кому выпадет король тот и стае Королем </i> ',
                           parse_mode="html",
                           reply_markup=kls)


######################
# _____Обработчик_____#
######################
@dp.message_handler(content_types=['text'])
async def lop(message):
    if message.chat.type == "private":
        #################################
        # __________Король Игрок_________#
        #################################
        if message.text == "Король Игрок 👑":
            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("3️⃣")
            cl4 = types.KeyboardButton("4️⃣")
            cl5 = types.KeyboardButton("5️⃣")
            cl6 = types.KeyboardButton("6️⃣")
            cl7 = types.KeyboardButton("7️⃣")
            cl8 = types.KeyboardButton("8️⃣")
            cl9 = types.KeyboardButton("9️⃣")
            cl10 = types.KeyboardButton("🔟")
            cln = types.KeyboardButton("⬅️Назад")
            kls.add(cl3, cl4, cl5, cl6, cl7, cl8, cl9, cl10, cln)
            await bot.send_message(message.chat.id, f"<b>Выберете количество игроков</b>",
                                   parse_mode="html",
                                   reply_markup=kls)

        # Кнопки игрока
        elif message.text == "3️⃣":
            d3 = random.choice(ch.list3)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GO3")
            cl32 = types.KeyboardButton("⬅Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)
        elif message.text == "4️⃣":
            d3 = random.choice(ch.list4)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GO4")
            cl32 = types.KeyboardButton("⬅Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        elif message.text == "5️⃣":
            d3 = random.choice(ch.list5)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GO5")
            cl32 = types.KeyboardButton("⬅Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        elif message.text == "6️⃣":
            d3 = random.choice(ch.list6)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GO6")
            cl32 = types.KeyboardButton("⬅Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        elif message.text == "7️⃣":
            d3 = random.choice(ch.list7)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GO7")
            cl32 = types.KeyboardButton("⬅Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        elif message.text == "8️⃣":
            d3 = random.choice(ch.list8)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GO8")
            cl32 = types.KeyboardButton("⬅Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        elif message.text == "9️⃣":
            d3 = random.choice(ch.list9)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GO9")
            cl32 = types.KeyboardButton("⬅Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        elif message.text == "🔟":
            d3 = random.choice(ch.list10)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GO10")
            cl32 = types.KeyboardButton("⬅Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        # Кнопки повтора Игрока
        elif message.text == "GO3":
            d3 = random.choice(ch.list3)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GO3")
            cl32 = types.KeyboardButton("⬅Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        elif message.text == "GO4":
            d3 = random.choice(ch.list4)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GO4")
            cl32 = types.KeyboardButton("⬅Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        elif message.text == "GO5":
            d3 = random.choice(ch.list5)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GO5")
            cl32 = types.KeyboardButton("⬅Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        elif message.text == "GO6":
            d3 = random.choice(ch.list6)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GO6")
            cl32 = types.KeyboardButton("⬅Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        elif message.text == "GO7":
            d3 = random.choice(ch.list7)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GO7")
            cl32 = types.KeyboardButton("⬅Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        elif message.text == "GO8":
            d3 = random.choice(ch.list8)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GO8")
            cl32 = types.KeyboardButton("⬅Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        elif message.text == "GO9":
            d3 = random.choice(ch.list9)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GO9")
            cl32 = types.KeyboardButton("⬅Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        elif message.text == "GO10":
            d3 = random.choice(ch.list10)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GO10")
            cl32 = types.KeyboardButton("⬅Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        ########################
        # _____Король БОТ_______#
        ########################
        if message.text == "Король Бот 🤖":
            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl2 = types.KeyboardButton("2️")
            cl3 = types.KeyboardButton("3️")
            cl4 = types.KeyboardButton("4️")
            cl5 = types.KeyboardButton("5️")
            cl6 = types.KeyboardButton("6️")
            cl7 = types.KeyboardButton("7️")
            cl8 = types.KeyboardButton("8️")
            cl9 = types.KeyboardButton("9️")
            cl10 = types.KeyboardButton("10")
            cln = types.KeyboardButton("⬅️Назад")
            kls.add(cl2, cl3, cl4, cl5, cl6, cl7, cl8, cl9, cl10, cln)
            await bot.send_message(message.chat.id, f"<b>Выберете количество игроков</b>",
                                   parse_mode="html",
                                   reply_markup=kls)

        # Кнопки БОТ
        elif message.text == "2️":
            d3 = random.choice(ch.listb2)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm2')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GOB2")
            cl32 = types.KeyboardButton("Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        elif message.text == "3️":
            d3 = random.choice(ch.listb3)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GOB3")
            cl32 = types.KeyboardButton("Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        elif message.text == "4️":
            d3 = random.choice(ch.listb4)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GOB4")
            cl32 = types.KeyboardButton("Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        elif message.text == "5️":
            d3 = random.choice(ch.listb5)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GOB5")
            cl32 = types.KeyboardButton("Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        elif message.text == "6️":
            d3 = random.choice(ch.listb6)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GOB6")
            cl32 = types.KeyboardButton("Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        elif message.text == "7️":
            d3 = random.choice(ch.listb7)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GOB7")
            cl32 = types.KeyboardButton("Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        elif message.text == "8️":
            d3 = random.choice(ch.listb8)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GOB8")
            cl32 = types.KeyboardButton("Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        elif message.text == "9️":
            d3 = random.choice(ch.listb9)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GOB9")
            cl32 = types.KeyboardButton("Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        elif message.text == "10":
            d3 = random.choice(ch.listb10)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GOB10")
            cl32 = types.KeyboardButton("Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        # Кнопки повтора БОТ
        elif message.text == "GOB2":
            d3 = random.choice(ch.listb2)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm2')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GOB2")
            cl32 = types.KeyboardButton("Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        elif message.text == "GOB3":
            d3 = random.choice(ch.listb3)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GOB3")
            cl32 = types.KeyboardButton("Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        elif message.text == "GOB4":
            d3 = random.choice(ch.listb4)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GOB4")
            cl32 = types.KeyboardButton("Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        elif message.text == "GOB5":
            d3 = random.choice(ch.listb5)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GOB5")
            cl32 = types.KeyboardButton("Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        elif message.text == "GOB6":
            d3 = random.choice(ch.listb6)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GOB6")
            cl32 = types.KeyboardButton("Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        elif message.text == "GOB7":
            d3 = random.choice(ch.listb7)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GOB7")
            cl32 = types.KeyboardButton("Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        elif message.text == "GOB8":
            d3 = random.choice(ch.listb8)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GOB8")
            cl32 = types.KeyboardButton("Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        elif message.text == "GOB9":
            d3 = random.choice(ch.listb9)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GOB9")
            cl32 = types.KeyboardButton("Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        elif message.text == "GOB10":
            d3 = random.choice(ch.listb10)

            clavain = types.InlineKeyboardMarkup(row_width=1)
            itm1 = types.InlineKeyboardButton("Желание", callback_data='itm1')
            clavain.add(itm1)

            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("GOB10")
            cl32 = types.KeyboardButton("Назад")
            kls.add(cl3, cl32)

            await bot.send_message(message.chat.id, f"Игроки № : {d3}", reply_markup=kls)
            await bot.send_message(message.chat.id, f"Желания для игрока:", reply_markup=clavain)

        # ДОНАТ
        elif message.text == "Донат💰":
            cl = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl32 = types.KeyboardButton("⬅️Назад")
            cl.add(cl32)
            kls = types.InlineKeyboardMarkup(row_width=1)
            itm = types.InlineKeyboardButton("Донат💰", url="https://prt.mn/balgWGXPiv")
            kls.add(itm)
            kol = open("sticker.webp", "rb")
            await bot.send_photo(message.chat.id, kol, reply_markup=cl)
            await bot.send_message(message.chat.id,
                                   "Этот недостойный разработчик будет очень благодарен, если ты пожертвуешь эму звонкую монетку так как он ещё довольно молод и вложил много средств времени и сил в этот проект. Буду очень благодарен за любую поддержку ❤",
                                   reply_markup=kls)


        ##################
        # Основные кнопки#
        ##################
        # start
        elif message.text == "⬅️Назад":
            pol = open("start.jpg", "rb")
            await bot.send_photo(message.chat.id, pol)
            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl1 = types.KeyboardButton("Король Игрок 👑")
            cl2 = types.KeyboardButton("Король Бот 🤖")
            cl3 = types.KeyboardButton("Донат💰")
            kls.add(cl1, cl2, cl3)
            await bot.send_message(message.chat.id,
                                   f"Добро пожаловать в наш скромный обитель господин <b>{message.from_user.first_name}</b>\n"
                                   "Ваш скромный слуга поможет вам и вашей свите сыграть в увлекательною игру\n"
                                   "<b>Для начала выберете один из предложенных режимов:</b>\n"
                                   "<b>1.</b><i>Король Игрок</i> = Король выбирается среди игроков и именно игрок отдает приказы либо запрашивает помощи у Бота\n"
                                   "<b>2.</b><i>Король Бот</i> = Король по умолчанию становиться Бот и именно бот назначает каму и какой приказ отдать \n"
                                   "Ознакомица с правилами /rules \n"
                                   "Помощь /help",
                                   parse_mode="html",
                                   reply_markup=kls)
        # Игрок король
        elif message.text == "⬅Назад":
            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl3 = types.KeyboardButton("3️⃣")
            cl4 = types.KeyboardButton("4️⃣")
            cl5 = types.KeyboardButton("5️⃣")
            cl6 = types.KeyboardButton("6️⃣")
            cl7 = types.KeyboardButton("7️⃣")
            cl8 = types.KeyboardButton("8️⃣")
            cl9 = types.KeyboardButton("9️⃣")
            cl10 = types.KeyboardButton("🔟")
            cln = types.KeyboardButton("⬅️Назад")
            kls.add(cl3, cl4, cl5, cl6, cl7, cl8, cl9, cl10, cln)
            await bot.send_message(message.chat.id, f"<b>Выберете количество игроков</b>",
                                   parse_mode="html",
                                   reply_markup=kls)
        # Король БОТ
        elif message.text == "Назад":
            kls = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cl2 = types.KeyboardButton("2️⃣")
            cl3 = types.KeyboardButton("3️⃣")
            cl4 = types.KeyboardButton("4️⃣")
            cl5 = types.KeyboardButton("5️⃣")
            cl6 = types.KeyboardButton("6️⃣")
            cl7 = types.KeyboardButton("7️⃣")
            cl8 = types.KeyboardButton("8️⃣")
            cl9 = types.KeyboardButton("9️⃣")
            cl10 = types.KeyboardButton("10")
            cln = types.KeyboardButton("⬅️Назад")
            kls.add(cl2, cl3, cl4, cl5, cl6, cl7, cl8, cl9, cl10, cln)
            await bot.send_message(message.chat.id, f"<b>Выберете количество игроков</b>",
                                   parse_mode="html",
                                   reply_markup=kls)


@dp.callback_query_handler(lambda query: True)
async def callback_inline(call):
    if call.message:
        # "___Инлайновая Кнопка1___"
        if call.data == 'itm1':
            dl = random.choice(txt.list)

            await bot.edit_message_text(chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        text=f"{dl}",
                                        reply_markup=None)  # Текст
        # "___Инлайновая Кнопка2___"
        elif call.data == 'itm2':
            dl = random.choice(txt.list2)

            await bot.edit_message_text(chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        text=f"{dl}",
                                        reply_markup=None)  # Текст


try:
    if __name__ == "__main__":
        executor.start_polling(dp, skip_updates=True)
except Exception:
    print("Ошыбка")
