from moviepy.editor import *
from pytube import YouTube


class Audio:
    CURRENT_DIR = os.getcwd()+'\\'

    def __init__(self, yt, mp4_files, filename=None):
        self.file_name = yt.title
        self.mp4_files = mp4_files
        self.yt = yt
        self.file = None

    async def check_correct_name(self):
        except_this = ['/', '\\', '|', ':', '<', '>', '*', '"', '?']
        for word in self.file_name:
            if word in except_this:
                self.file_name = self.file_name.replace(word, '')

    async def download_video(self):
        mp4_144p_files = self.mp4_files.get_by_resolution("360p")
        await self.check_correct_name()

        try:
            mp4_144p_files.download(filename=self.file_name + ".mp4")
        except OSError as IA:
            mp4_144p_files.download()

    async def convert_to_mp3(self):
        await self.download_video()
        video = VideoFileClip(os.path.join(self.CURRENT_DIR + self.file_name + ".mp4"))
        video.audio.write_audiofile(os.path.join(self.file_name + ".mp3"))
        video.close()

        return open(self.file_name + ".mp3", 'rb')

    def __del__(self):
        try:
            os.remove(self.CURRENT_DIR + self.file_name + ".mp4")
            os.remove(self.CURRENT_DIR + self.file_name + ".mp3")
        except Exception as e:
            print(e)


async def check_url(url: str):
    try:
        yt = YouTube(url)
        mp4_files = yt.streams.filter(file_extension="mp4")
        return yt, mp4_files
    except Exception as e:
        print(e)
        return None, None