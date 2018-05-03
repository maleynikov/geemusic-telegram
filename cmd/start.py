from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton

from gmusic import Client


def cmd_start(bot, update):
    song = Client().get_random_song()
    help_text = 'I can help you find and share any music. Just send me a query like: _{0}_.'.format(song['title'])
    keyboard = [[InlineKeyboardButton('Send music to friends', switch_inline_query='')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(help_text, reply_markup=reply_markup, parse_mode=ParseMode.MARKDOWN)
