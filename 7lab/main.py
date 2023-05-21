import datetime

import telebot
from telebot import types
import psycopg2

conn = psycopg2.connect(database="tgbot_db", user="postgres", password="1804#Mtn", host="localhost", port="5432")
cursor = conn.cursor()

token = "6043107428:AAGTBH29OtPUBoXVpcKhvDm8MRK4UekM7kM"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/help", "Понедельник", "Вторник")
    keyboard.row("Среда", "Четверг", "Пятница", "Суббота")
    keyboard.row("Расписание на текущую неделю", "Расписание на следующую неделю")
    bot.send_message(message.chat.id, 'Привет! Хотите узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Я умею определять неделю - /week \nЯ умею направлять на главную страницу - /mtuci \n Я умею показывать расписание группы БВТ2202 просто скажите мне на какой день недели или на какую неделю')


@bot.message_handler(commands=['week'])
def start_message(message):
    today = datetime.date.today()
    week_numb = today.isocalendar()[1]
    if week_numb % 2 == 0:
        bot.send_message(message.chat.id, 'Текущая неделя четная')
    else:
        bot.send_message(message.chat.id, 'Текущая неделя нечетная')


@bot.message_handler(commands=['mtuci'])
def start_message(message):
    bot.send_message(message.chat.id, 'Тебе сюда - https://mtuci.ru/')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "расписание на следующую неделю":
        today = datetime.date.today()
        week_numb = today.isocalendar()[1]
        week_numb %= 2
        if week_numb == 0:
            cursor.execute("SELECT * FROM timetable WHERE day = 'Понедельник' AND week = 'Нечетная'")
            records = list(cursor.fetchall())
            if records:
                txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
                i = 0
                x = len(records)
                while i < x:
                    txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                    cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                    records1 = list(cursor.fetchall())
                    txt += records1[0][1] + '\n'
                    i += 1
                bot.send_message(message.chat.id, txt)
            else:
                bot.send_message(message.chat.id, "Понедельник нечетной недели свободен")

            cursor.execute("SELECT * FROM timetable WHERE day = 'Вторник' AND week = 'Нечетная'")
            records = list(cursor.fetchall())
            if records:
                txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
                i = 0
                x = len(records)
                while i < x:
                    txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                    cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                    records1 = list(cursor.fetchall())
                    txt += records1[0][1] + '\n'
                    i += 1
                bot.send_message(message.chat.id, txt)
            else:
                bot.send_message(message.chat.id, "Вторник нечетной недели свободен")

            cursor.execute("SELECT * FROM timetable WHERE day = 'Среда' AND week = 'Нечетная'")
            records = list(cursor.fetchall())
            if records:
                txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
                i = 0
                x = len(records)
                while i < x:
                    txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                    cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                    records1 = list(cursor.fetchall())
                    txt += records1[0][1] + '\n'
                    i += 1
                bot.send_message(message.chat.id, txt)
            else:
                bot.send_message(message.chat.id, "Среда нечетной недели свободна")

            cursor.execute("SELECT * FROM timetable WHERE day = 'Четверг' AND week = 'Нечетная'")
            records = list(cursor.fetchall())
            if records:
                txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
                i = 0
                x = len(records)
                while i < x:
                    txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                    cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                    records1 = list(cursor.fetchall())
                    txt += records1[0][1] + '\n'
                    i += 1
                bot.send_message(message.chat.id, txt)
            else:
                bot.send_message(message.chat.id, "Четверг нечетной недели свободен")

            cursor.execute("SELECT * FROM timetable WHERE day = 'Пятница' AND week = 'Нечетная'")
            records = list(cursor.fetchall())
            if records:
                txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
                i = 0
                x = len(records)
                while i < x:
                    txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                    cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                    records1 = list(cursor.fetchall())
                    txt += records1[0][1] + '\n'
                    i += 1
                bot.send_message(message.chat.id, txt)
            else:
                bot.send_message(message.chat.id, "Пятница нечетной недели свободна")

            cursor.execute("SELECT * FROM timetable WHERE day = 'Суббота' AND week = 'Нечетная'")
            records = list(cursor.fetchall())
            if records:
                txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
                i = 0
                x = len(records)
                while i < x:
                    txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                    cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                    records1 = list(cursor.fetchall())
                    txt += records1[0][1] + '\n'
                    i += 1
                bot.send_message(message.chat.id, txt)
            else:
                bot.send_message(message.chat.id, "Суббота нечетной недели свободна")

        else:
            cursor.execute("SELECT * FROM timetable WHERE day = 'Понедельник' AND week = 'Четная'")
            records = list(cursor.fetchall())
            if records:
                txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
                i = 0
                x = len(records)
                while i < x:
                    txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                    cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                    records1 = list(cursor.fetchall())
                    txt += records1[0][1] + '\n'
                    i += 1
                bot.send_message(message.chat.id, txt)
            else:
                bot.send_message(message.chat.id, "Понедельник четной недели свободен")

            cursor.execute("SELECT * FROM timetable WHERE day = 'Вторник' AND week = 'Четная'")
            records = list(cursor.fetchall())
            if records:
                txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
                i = 0
                x = len(records)
                while i < x:
                    txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                    cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                    records1 = list(cursor.fetchall())
                    txt += records1[0][1] + '\n'
                    i += 1
                bot.send_message(message.chat.id, txt)
            else:
                bot.send_message(message.chat.id, "Вторник четной недели свободен")

            cursor.execute("SELECT * FROM timetable WHERE day = 'Среда' AND week = 'Четная'")
            records = list(cursor.fetchall())
            if records:
                txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
                i = 0
                x = len(records)
                while i < x:
                    txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                    cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                    records1 = list(cursor.fetchall())
                    txt += records1[0][1] + '\n'
                    i += 1
                bot.send_message(message.chat.id, txt)
            else:
                bot.send_message(message.chat.id, "Среда четной недели свободна")

            cursor.execute("SELECT * FROM timetable WHERE day = 'Четверг' AND week = 'Четная'")
            records = list(cursor.fetchall())
            if records:
                txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
                i = 0
                x = len(records)
                while i < x:
                    txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                    cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                    records1 = list(cursor.fetchall())
                    txt += records1[0][1] + '\n'
                    i += 1
                bot.send_message(message.chat.id, txt)
            else:
                bot.send_message(message.chat.id, "Четверг четной недели свободен")

            cursor.execute("SELECT * FROM timetable WHERE day = 'Пятница' AND week = 'Четная'")
            records = list(cursor.fetchall())
            if records:
                txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
                i = 0
                x = len(records)
                while i < x:
                    txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                    cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                    records1 = list(cursor.fetchall())
                    txt += records1[0][1] + '\n'
                    i += 1
                bot.send_message(message.chat.id, txt)
            else:
                bot.send_message(message.chat.id, "Пятница четной недели свободна")

            cursor.execute("SELECT * FROM timetable WHERE day = 'Суббота' AND week = 'Четная'")
            records = list(cursor.fetchall())
            if records:
                txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
                i = 0
                x = len(records)
                while i < x:
                    txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                    cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                    records1 = list(cursor.fetchall())
                    txt += records1[0][1] + '\n'
                    i += 1
                bot.send_message(message.chat.id, txt)
            else:
                bot.send_message(message.chat.id, "Суббота четной недели свободна")
    elif message.text.lower() == "расписание на текущую неделю":
        today = datetime.date.today()
        week_numb = today.isocalendar()[1]
        week_numb %= 2
        if week_numb != 0:
            cursor.execute("SELECT * FROM timetable WHERE day = 'Понедельник' AND week = 'Нечетная'")
            records = list(cursor.fetchall())
            if records:
                txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
                i = 0
                x = len(records)
                while i < x:
                    txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                    cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                    records1 = list(cursor.fetchall())
                    txt += records1[0][1] + '\n'
                    i += 1
                bot.send_message(message.chat.id, txt)
            else:
                bot.send_message(message.chat.id, "Понедельник нечетной недели свободен")

            cursor.execute("SELECT * FROM timetable WHERE day = 'Вторник' AND week = 'Нечетная'")
            records = list(cursor.fetchall())
            if records:
                txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
                i = 0
                x = len(records)
                while i < x:
                    txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                    cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                    records1 = list(cursor.fetchall())
                    txt += records1[0][1] + '\n'
                    i += 1
                bot.send_message(message.chat.id, txt)
            else:
                bot.send_message(message.chat.id, "Вторник нечетной недели свободен")

            cursor.execute("SELECT * FROM timetable WHERE day = 'Среда' AND week = 'Нечетная'")
            records = list(cursor.fetchall())
            if records:
                txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
                i = 0
                x = len(records)
                while i < x:
                    txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                    cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                    records1 = list(cursor.fetchall())
                    txt += records1[0][1] + '\n'
                    i += 1
                bot.send_message(message.chat.id, txt)
            else:
                bot.send_message(message.chat.id, "Среда нечетной недели свободна")

            cursor.execute("SELECT * FROM timetable WHERE day = 'Четверг' AND week = 'Нечетная'")
            records = list(cursor.fetchall())
            if records:
                txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
                i = 0
                x = len(records)
                while i < x:
                    txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                    cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                    records1 = list(cursor.fetchall())
                    txt += records1[0][1] + '\n'
                    i += 1
                bot.send_message(message.chat.id, txt)
            else:
                bot.send_message(message.chat.id, "Четверг нечетной недели свободен")

            cursor.execute("SELECT * FROM timetable WHERE day = 'Пятница' AND week = 'Нечетная'")
            records = list(cursor.fetchall())
            if records:
                txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
                i = 0
                x = len(records)
                while i < x:
                    txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                    cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                    records1 = list(cursor.fetchall())
                    txt += records1[0][1] + '\n'
                    i += 1
                bot.send_message(message.chat.id, txt)
            else:
                bot.send_message(message.chat.id, "Пятница нечетной недели свободна")

            cursor.execute("SELECT * FROM timetable WHERE day = 'Суббота' AND week = 'Нечетная'")
            records = list(cursor.fetchall())
            if records:
                txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
                i = 0
                x = len(records)
                while i < x:
                    txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                    cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                    records1 = list(cursor.fetchall())
                    txt += records1[0][1] + '\n'
                    i += 1
                bot.send_message(message.chat.id, txt)
            else:
                bot.send_message(message.chat.id, "Суббота нечетной недели свободна")

        else:
            cursor.execute("SELECT * FROM timetable WHERE day = 'Понедельник' AND week = 'Четная'")
            records = list(cursor.fetchall())
            if records:
                txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
                i = 0
                x = len(records)
                while i < x:
                    txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                    cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                    records1 = list(cursor.fetchall())
                    txt += records1[0][1] + '\n'
                    i += 1
                bot.send_message(message.chat.id, txt)
            else:
                bot.send_message(message.chat.id, "Понедельник четной недели свободен")

            cursor.execute("SELECT * FROM timetable WHERE day = 'Вторник' AND week = 'Четная'")
            records = list(cursor.fetchall())
            if records:
                txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
                i = 0
                x = len(records)
                while i < x:
                    txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                    cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                    records1 = list(cursor.fetchall())
                    txt += records1[0][1] + '\n'
                    i += 1
                bot.send_message(message.chat.id, txt)
            else:
                bot.send_message(message.chat.id, "Вторник четной недели свободен")

            cursor.execute("SELECT * FROM timetable WHERE day = 'Среда' AND week = 'Четная'")
            records = list(cursor.fetchall())
            if records:
                txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
                i = 0
                x = len(records)
                while i < x:
                    txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                    cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                    records1 = list(cursor.fetchall())
                    txt += records1[0][1] + '\n'
                    i += 1
                bot.send_message(message.chat.id, txt)
            else:
                bot.send_message(message.chat.id, "Среда четной недели свободна")

            cursor.execute("SELECT * FROM timetable WHERE day = 'Четверг' AND week = 'Четная'")
            records = list(cursor.fetchall())
            if records:
                txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
                i = 0
                x = len(records)
                while i < x:
                    txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                    cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                    records1 = list(cursor.fetchall())
                    txt += records1[0][1] + '\n'
                    i += 1
                bot.send_message(message.chat.id, txt)
            else:
                bot.send_message(message.chat.id, "Четверг четной недели свободен")

            cursor.execute("SELECT * FROM timetable WHERE day = 'Пятница' AND week = 'Четная'")
            records = list(cursor.fetchall())
            if records:
                txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
                i = 0
                x = len(records)
                while i < x:
                    txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                    cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                    records1 = list(cursor.fetchall())
                    txt += records1[0][1] + '\n'
                    i += 1
                bot.send_message(message.chat.id, txt)
            else:
                bot.send_message(message.chat.id, "Пятница четной недели свободна")

            cursor.execute("SELECT * FROM timetable WHERE day = 'Суббота' AND week = 'Четная'")
            records = list(cursor.fetchall())
            if records:
                txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
                i = 0
                x = len(records)
                while i < x:
                    txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                    cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                    records1 = list(cursor.fetchall())
                    txt += records1[0][1] + '\n'
                    i += 1
                bot.send_message(message.chat.id, txt)
            else:
                bot.send_message(message.chat.id, "Суббота четной недели свободна")

    elif message.text.lower() == "понедельник":
        cursor.execute("SELECT * FROM timetable WHERE day = 'Понедельник' AND week = 'Нечетная'")
        records = list(cursor.fetchall())
        if records:
            txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
            i = 0
            x = len(records)
            while i < x:
                txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                records1 = list(cursor.fetchall())
                txt += records1[0][1] + '\n'
                i += 1
            bot.send_message(message.chat.id, txt)
        else:
            bot.send_message(message.chat.id, "Понедельник нечетной недели свободен")

        cursor.execute("SELECT * FROM timetable WHERE day = 'Понедельник' AND week = 'Четная'")
        records = list(cursor.fetchall())
        if records:
            txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
            i = 0
            x = len(records)
            while i < x:
                txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                records1 = list(cursor.fetchall())
                txt += records1[0][1] + '\n'
                i += 1
            bot.send_message(message.chat.id, txt)
        else:
            bot.send_message(message.chat.id, "Понедельник четной недели свободен")

    elif message.text.lower() == "вторник":
        cursor.execute("SELECT * FROM timetable WHERE day = 'Вторник' AND week = 'Нечетная'")
        records = list(cursor.fetchall())
        if records:
            txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
            i = 0
            x = len(records)
            while i < x:
                txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                records1 = list(cursor.fetchall())
                txt += records1[0][1] + '\n'
                i += 1
            bot.send_message(message.chat.id, txt)
        else:
            bot.send_message(message.chat.id, "Вторник нечетной недели свободен")

        cursor.execute("SELECT * FROM timetable WHERE day = 'Вторник' AND week = 'Четная'")
        records = list(cursor.fetchall())
        if records:
            txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
            i = 0
            x = len(records)
            while i < x:
                txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                records1 = list(cursor.fetchall())
                txt += records1[0][1] + '\n'
                i += 1
            bot.send_message(message.chat.id, txt)
        else:
            bot.send_message(message.chat.id, "Вторник четной недели свободен")

    elif message.text.lower() == "среда":
        cursor.execute("SELECT * FROM timetable WHERE day = 'Среда' AND week = 'Нечетная'")
        records = list(cursor.fetchall())
        if records:
            txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
            i = 0
            x = len(records)
            while i < x:
                txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                records1 = list(cursor.fetchall())
                txt += records1[0][1] + '\n'
                i += 1
            bot.send_message(message.chat.id, txt)
        else:
            bot.send_message(message.chat.id, "Среда нечетной недели свободна")

        cursor.execute("SELECT * FROM timetable WHERE day = 'Среда' AND week = 'Четная'")
        records = list(cursor.fetchall())
        if records:
            txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
            i = 0
            x = len(records)
            while i < x:
                txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                records1 = list(cursor.fetchall())
                txt += records1[0][1] + '\n'
                i += 1
            bot.send_message(message.chat.id, txt)
        else:
            bot.send_message(message.chat.id, "Среда четной недели свободна")

    elif message.text.lower() == "четверг":
        cursor.execute("SELECT * FROM timetable WHERE day = 'Четверг' AND week = 'Нечетная'")
        records = list(cursor.fetchall())
        if records:
            txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
            i = 0
            x = len(records)
            while i < x:
                txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                records1 = list(cursor.fetchall())
                txt += records1[0][1] + '\n'
                i += 1
            bot.send_message(message.chat.id, txt)
        else:
            bot.send_message(message.chat.id, "Четверг нечетной недели свободен")

        cursor.execute("SELECT * FROM timetable WHERE day = 'Четверг' AND week = 'Четная'")
        records = list(cursor.fetchall())
        if records:
            txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
            i = 0
            x = len(records)
            while i < x:
                txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                records1 = list(cursor.fetchall())
                txt += records1[0][1] + '\n'
                i += 1
            bot.send_message(message.chat.id, txt)
        else:
            bot.send_message(message.chat.id, "Четверг четной недели свободен")

    elif message.text.lower() == "пятница":
        cursor.execute("SELECT * FROM timetable WHERE day = 'Пятница' AND week = 'Нечетная'")
        records = list(cursor.fetchall())
        if records:
            txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
            i = 0
            x = len(records)
            while i < x:
                txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                records1 = list(cursor.fetchall())
                txt += records1[0][1] + '\n'
                i += 1
            bot.send_message(message.chat.id, txt)
        else:
            bot.send_message(message.chat.id, "Пятница нечетной недели свободна")

        cursor.execute("SELECT * FROM timetable WHERE day = 'Пятница' AND week = 'Четная'")
        records = list(cursor.fetchall())
        if records:
            txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
            i = 0
            x = len(records)
            while i < x:
                txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                records1 = list(cursor.fetchall())
                txt += records1[0][1] + '\n'
                i += 1
            bot.send_message(message.chat.id, txt)
        else:
            bot.send_message(message.chat.id, "Пятница четной недели свободна")

    elif message.text.lower() == "суббота":
        cursor.execute("SELECT * FROM timetable WHERE day = 'Суббота' AND week = 'Нечетная'")
        records = list(cursor.fetchall())
        if records:
            txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
            i = 0
            x = len(records)
            while i < x:
                txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                records1 = list(cursor.fetchall())
                txt += records1[0][1] + '\n'
                i += 1
            bot.send_message(message.chat.id, txt)
        else:
            bot.send_message(message.chat.id, "Суббота нечетной недели свободна")

        cursor.execute("SELECT * FROM timetable WHERE day = 'Суббота' AND week = 'Четная'")
        records = list(cursor.fetchall())
        if records:
            txt = records[0][1] + ' ' + records[0][5] + ' неделя\n'
            i = 0
            x = len(records)
            while i < x:
                txt += records[i][2] + ' ' + records[i][3] + ' ' + records[0][4] + ' '
                cursor.execute("SELECT * FROM teacher WHERE subject = '" + records[i][2] + "'")
                records1 = list(cursor.fetchall())
                txt += records1[0][1] + '\n'
                i += 1
            bot.send_message(message.chat.id, txt)
        else:
            bot.send_message(message.chat.id, "Суббота четной недели свободна")
    else:
        bot.send_message(message.chat.id, "Я Вас не понимаю")


bot.polling(none_stop=True)
