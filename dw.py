from moviepy.editor import *
from pytube import YouTube


class Audio:
    CURRENT_DIR = os.getcwd()+'\\'

    def __init__(self, url, filename=None):
        self.file_name = filename
        self.url = url
        self.mp4_files = None
        self.yt = None
        self.file = None

    def check_url(self):
        try:
            print(self.url)
            self.yt = YouTube(self.url)
            self.mp4_files = self.yt.streams.filter(file_extension="mp4")
            return True
        except Exception as e:
            print(e)
            return False


    def download_video(self):
        mp4_144p_files = self.mp4_files.get_by_resolution("360p")

        if not self.file_name:
            self.file_name = self.yt.title
        mp4_144p_files.download(filename=self.file_name + ".mp4")

    def convert_to_mp3(self):
        video = VideoFileClip(os.path.join(self.CURRENT_DIR + self.file_name + ".mp4"))
        video.audio.write_audiofile(os.path.join(self.file_name + ".mp3"))

        self.file = open(self.file_name + ".mp3", 'rb')

    def __del__(self):
        print('destructor was called')
        try:
            os.remove(self.CURRENT_DIR + self.file_name + ".mp4")
            os.remove(self.CURRENT_DIR + self.file_name + ".mp3")
        except:
            pass
