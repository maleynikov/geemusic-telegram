from telegram import (ParseMode,
                      InlineKeyboardMarkup,
                      InlineKeyboardButton, Update)
from telegram.ext import CallbackContext

from gmusic import Client

client = Client()


def command(update: Update, context: CallbackContext):
    song = client.get_random_song()
    help_text = 'I can help you search and share any music. ' \
                'Just send me a query like: _{0}_.'.format(song['title'])
    keyboard = [
        [InlineKeyboardButton('Send music to friends', switch_inline_query='')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(help_text, reply_markup=reply_markup, parse_mode=ParseMode.MARKDOWN)
