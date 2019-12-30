from telegram import InlineQueryResultAudio, Update
from telegram.ext import CallbackContext

from gmusic import Client
from config import Config

config = Config()


def inlinequery(update: Update, context: CallbackContext):
    client = Client()
    results = []

    for song in client.search_songs(update.inline_query.query):
        results.append(InlineQueryResultAudio(
            id=song['nid'],
            title=song['title'],
            performer=song['artist'],
            audio_duration=song['duration'],
            audio_url='https://{0}/get_song?id=T{1}'.format(config.get_option('proxy', 'host'), song['nid'])
        ))

    update.inline_query.answer(results)
