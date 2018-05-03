from telegram import ParseMode
from gmusic import Client


def cmd_find(bot, update):
    FindCommand().execute(bot, update)


class FindCommand(object):

    def __init__(self):
        self.client = Client()

    def execute(self, bot, update):
        songs = []

        for song in self.client.search_songs(update.message.text):
            songs.append(u'*{0}*\n{1}\n_Download:_ /dl\_{2}'.format(
                song['artist'],
                song['title'],
                song['nid']
            ))

        if len(songs) > 0:
            update.message.reply_text(text='\n\n'.join(songs), parse_mode=ParseMode.MARKDOWN)
        else:
            update.message.reply_text('No fack, no luck.')
