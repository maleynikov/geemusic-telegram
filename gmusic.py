from gmusicapi import Mobileclient
import config


class Client(object):

    def __init__(self):
        self.client = Mobileclient()
        self.client.login(config.gmusic['email'], config.gmusic['password'], config.gmusic['device_id'])

    def search_songs(self, query_str):
        song_hits = self.client.search(query_str, 10)['song_hits']
        songs = []

        for song_hit in song_hits:
            songs.append({
                'title': song_hit['track']['title'],
                'artist': song_hit['track']['artist'],
                'album': song_hit['track']['album'],
                'nid': song_hit['track']['nid'],
            })

        return songs

    @staticmethod
    def __prepare_nid(nid):
        return 'T{0}'.format(nid)

    def get_song_url(self, nid):
        return self.client.get_stream_url(self.__prepare_nid(nid))

    def get_song_info(self, nid):
        return self.client.get_track_info(self.__prepare_nid(nid))
