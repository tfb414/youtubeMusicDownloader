#!/usr/bin/env python3

from youtube_api import YouTubeDataAPI
from datetime import datetime, timedelta
from pytube import YouTube
import re
import numpy

SAVED_SONGS_FILE = "songIds.txt"
API_KEY = 'fix me'

now = datetime.now()
time_minus_one_month = (datetime.now() - timedelta(30)).strftime('%Y, %m, %d')

time_array = time_minus_one_month.split(',')
INT_TIME_ARRAY = list(map(lambda time: int(time), time_array))


def get_already_saved_song_ids(file_name):
    with open(file_name) as f:
        contents = f.read().strip()
        song_ids = list(contents.split(','))

        return song_ids


def add_song_id(file_name, id):
    f = open(file_name, "a")
    f.write(id + ",")
    f.close()


def get_recent_song_ids(INT_TIME_ARRAY):
    yt = YouTubeDataAPI(API_KEY)

    all_song_info = yt.get_videos_from_playlist_id(
        'PL63ZO-jXFTasqvj7WdEFQ6QtG6UBrl9CR',
        published_after=datetime(INT_TIME_ARRAY[0],
                                 INT_TIME_ARRAY[1],
                                 INT_TIME_ARRAY[2])
    )
    return select_ids(all_song_info)


def select_ids(all_song_info):
    return list(map(lambda song_info: song_info['video_id'], all_song_info))


def get_songs_to_download():
    previously_downloaded_ids = get_already_saved_song_ids(
        SAVED_SONGS_FILE)
    recent_song_ids = get_recent_song_ids(INT_TIME_ARRAY)

    songs_to_download = []
    for id in recent_song_ids:
        if(id not in previously_downloaded_ids):
            songs_to_download.append(id)

    return songs_to_download


def download_song(song_id):
    url = f'https://www.youtube.com/watch?v={song_id}'
    yt = YouTube(url)
    streams = yt.streams.filter(only_audio=True).all()
    stream_quality = []

    for stream in streams:
        quality = re.findall(r'\d+', stream.abr)
        stream_quality.append(int(quality[0]))

    fastest_stream = numpy.argmax(stream_quality)

    print(f'starting download for {song_id}')
    yt.streams.get_by_itag(streams[fastest_stream].itag).download('tmp')
    print(f'{song_id} downloaded successfully')


def main():
    songs_to_download = get_songs_to_download()
    print(songs_to_download)
    for song in songs_to_download:
        download_song(song)
        add_song_id('songIds.txt', song)


main()
