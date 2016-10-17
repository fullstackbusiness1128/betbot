import os
import json

from aiotg import Bot

bot = Bot(api_token=os.environ['API_KEY'])


@bot.command(r'/start')
def start(chat, match):
    markup = {
        "keyboard": [["Make a bet"], ["Show rating"], ["Your bets"]],
        "one_time_keyboard": True
    }
    return chat.send_text('Hello! Please make a bet. Your balance: 1000', reply_markup=json.dumps(markup))


@bot.command(r'/choose_sport')
def choose_sport(chat, match):
    return chat.send_text('Ok, choose sport')


@bot.command(r'/sport (.+)')
def sport(chat, match):
    return chat.send_text('Wow! {} is a good choice'.format(match.group(1)))


@bot.command(r'/champ (.+)')
def championship(chat, match):
    return chat.send_text('Great! You chose {}. Luck is on your side. Choose a game.'.format(match.group(1)))


@bot.command(r'/game (.+)')
def game(chat, match):
    return chat.send_text('Great game! Coeffs are (1 - X - 2) : (1,26 - 2,34 - 2,75)')


@bot.command(r'/makebet (.+)')
def make_bet(chat, match):
    return chat.send_text('Accepted! You will be noticed about results')


@bot.command(r'/result')
def sport(chat, match):
    return chat.send_text('Your bet won!!! Your balance: 1026')

bot.run()
