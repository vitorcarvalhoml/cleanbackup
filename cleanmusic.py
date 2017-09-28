#! -*- coding: utf-8 -*-

import os
from mutagen.mp3 import MP3

class CleanMusic():

    def __init__(self):
        music_path = None 
        music_length = None
        music_name = str()
        music_author = str()

    def setProperties(self, music_path):
        self.mi = MP3(music_path)
        self.music_path = music_path
        self.music_length = self.mi.info.length

    def clean(self):
        if self.music_length == None:
            self.setProperties()
        if self.music_length <= 10:
            try:
                os.remove(self.music_path)
            except FileNotFoundError:
                print("File does not exist")

    def destroy(self):
        pass
