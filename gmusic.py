from gmusicapi import Mobileclient
from random import choice
import config


class Client(object):
    __instance = None

    def __new__(cls):
        if Client.__instance is None:
            Client.__instance = object.__new__(cls)
            Client.__instance.client = Mobileclient()
            Client.__instance.client.login(
                email=config.gmusic['email'],
                password=config.gmusic['password'],
                android_id=config.gmusic['device_id']
            )

        return Client.__instance

    def search_songs(self, query_str):
        song_hits = self.client.search(query_str, config.gmusic['search_result_max_cnt'])['song_hits']
        songs = []

        for song_hit in song_hits:
            songs.append({
                'title': song_hit['track']['title'],
                'artist': song_hit['track']['artist'],
                'album': song_hit['track']['album'],
                'nid': song_hit['track']['nid'],
                'duration': int(float(song_hit['track']['durationMillis']) / 1000)
            })

        return songs

    @staticmethod
    def __prepare_nid(nid):
        return 'T{0}'.format(nid)

    def get_song_url(self, nid):
        return self.client.get_stream_url(self.__prepare_nid(nid))

    def get_song_info(self, nid):
        return self.client.get_track_info(self.__prepare_nid(nid))

    def get_random_song(self):
        songs = self.client.get_all_songs()

        return choice(songs)
