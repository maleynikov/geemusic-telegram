from telegram import Update
from telegram.ext import CallbackContext

from gmusic import Client
from .dl import Download

client = Client()


def command(update: Update, context: CallbackContext):
    song = client.get_random_song()
    song_nid = song['nid'].replace('T', '')

    # download random song
    Download(song_nid).execute(update)
