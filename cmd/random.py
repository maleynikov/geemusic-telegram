from gmusic import Client
from .dl import DlCommand


def cmd_random(bot, update):
    song = Client().get_random_song()
    song_nid = song['nid'].replace('T', '')

    # download random song
    DlCommand(song_nid).execute(bot, update)
