from re import L
import telebot
import random

YEAR  = 365 * 24 * 60 * 60
MONTH = 30 * 24 * 60 * 60
DAY   = 24 * 60 * 60
HOUR  = 60 * 60

def num_ending(n):
    if 20 > n > 10:
        return 2
    if n % 10 == 1:
        return 0
    if n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
        return 1
    return 2

def hum_t(t):
    y = t // YEAR
    t %= YEAR
    m = t // MONTH
    t %= MONTH
    d = t // DAY
    t %= DAY

    y_vars = ['год', 'года', 'лет']
    m_vars = ['месяц', 'месяца', 'месяцев']
    d_vars = ['день', 'дня', 'дней']
    #h_vars = ['час', 'часа', 'часов']
    
    rep = ''
    if y != 0:
        rep += str(y) + ' ' + y_vars[num_ending(y)] + ' '
    if m != 0:
        if d == 0 and len(rep):
            rep += 'и '
        rep += str(m) + ' ' + m_vars[num_ending(m)] + ' '
    if d != 0:
        if  len(rep):
            rep += 'и '
        rep += str(d) + ' ' + d_vars[num_ending(d)]
    if len(rep) == 0:
        rep = '0 секунд!!!'
    return rep

bot = telebot.TeleBot('5173516150:AAFQGh_mrCsRhKuIQJ_7NqZ2TJI67qSknoU')

@bot.message_handler(commands=['start'])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет, это отсос бот')

@bot.inline_handler(lambda query: True)
def query_text(inline_query):
    try:
        t = random.randrange(0, 150_000_000, 1)
        user = inline_query.from_user.username
        person = 'Кто прочитал тот'
        if inline_query.query.strip() != '':
            person = inline_query.query.strip()
        reply = person + ' отсосёт хуй у @' + user + ' через ' + hum_t(t)
        r = telebot.types.InlineQueryResultArticle('1', 'Предсказание...', telebot.types.InputTextMessageContent(reply))
        bot.answer_inline_query(inline_query.id, [r], cache_time=0)
    except Exception as e:
        print(e)

bot.polling(none_stop=True, interval=0)