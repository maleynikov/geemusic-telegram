from telegram import InlineQueryResultAudio
from gmusic import Client
import config


def inlinequery(bot, update):
    client = Client()
    results = []

    for song in client.search_songs(update.inline_query.query):
        results.append(InlineQueryResultAudio(
            id=song['nid'],
            title=song['title'],
            performer=song['artist'],
            audio_duration=song['duration'],
            audio_url='{0}/get_song?id=T{1}'.format(config.gmusic['proxy_server'], song['nid'])
        ))

    update.inline_query.answer(results)
