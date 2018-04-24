import hashlib
import requests
from mutagen.id3 import ID3, TIT2, TPE1, APIC
from mutagen.mp3 import MP3, error
from gmusic import Client


def cmd_dl(bot, update, groups):
    DlCommand(groups[0]).execute(bot, update)


class DlCommand(object):

    def __init__(self, song_nid):
        self.song_nid = song_nid
        self.client = Client()

    @staticmethod
    def __song_download(song_url):
        response = requests.get(song_url)

        if response.status_code == requests.codes.ok:
            filename = hashlib.md5(song_url.encode('utf-8')).hexdigest()
            filepath = '/tmp/geemusicbot_{0}.mp3'.format(filename)

            with open(filepath, 'wb') as out:
                out.write(response.content)

            return dict(filename=filename, filepath=filepath)

        return None

    @staticmethod
    def __bind_tags(song_file, song_info):
        audio = MP3(song_file['filepath'], ID3=ID3)
        
        try:
            audio.add_tags()
        except error:
            pass

        # set title
        audio.tags.add(TIT2(encoding=3, text=song_info['title']))

        # set artist
        audio.tags.add(TPE1(encoding=3, text=song_info['artist']))

        # set album cover
        response = requests.get(song_info['albumArtRef'][0]['url'])
        filepath = '/tmp/geemusicbot_{0}.jpg'.format(song_file['filename'])

        with open(filepath, 'wb') as out:
            out.write(response.content)

        audio.tags.add(APIC(
            encoding=3,
            mime='image/jpeg',
            type=3,
            desc='Album cover',
            data=open(filepath, 'rb').read()
        ))
        audio.save(v2_version=3)

    def execute(self, bot, update):
        song_url = self.client.get_song_url(self.song_nid)
        song_file = self.__song_download(song_url)
        song_info = self.client.get_song_info(self.song_nid)

        self.__bind_tags(song_file, song_info)

        if song_file is not None:
            audio = open(song_file['filepath'], 'rb')
            bot.send_audio(chat_id=update.message.chat_id, audio=audio)
