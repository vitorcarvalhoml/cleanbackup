#! -*- coding: utf-8 -*-

import os
from cleanmusic import CleanMusic 

if __name__ == '__main__':
    musics_path = "/Users/vitor/Projects/cleanbackup/tests"
    #musics_path = input("set music path: ")
    try:
        files = os.listdir(musics_path)
        musics = [os.path.abspath(os.path.join(musics_path, f)) for f in files]
    except FileNotFoundError:
        # remove print and add log file
        print("directory doest not exist")

    cm = CleanMusic()
    for music_path in musics:
        cm.setProperties(music_path)
        print(cm.music_length)
        
