import io
from pytube import YouTube


class Audio:

    def __init__(self, yt, mp4_file, filename=None):
        self.file_name = yt.title
        self.mp4_audio = mp4_file
        self.yt = yt
        self.file = None

    async def check_correct_name(self):
        except_this = ['/', '\\', '|', ':', '<', '>', '*', '"', '?']
        for word in self.file_name:
            if word in except_this:
                self.file_name = self.file_name.replace(word, '')

    async def download_video(self):
        await self.check_correct_name()

        try:
            b = io.BytesIO()
            self.mp4_audio.stream_to_buffer(b)
            return b.getbuffer(), self.file_name
        except OSError as IA:
            self.mp4_audio.download()

        return open(self.file_name + ".mp3", 'rb')


async def check_url(url: str):
    try:
        yt = YouTube(url)
        mp4_files = yt.streams.filter(only_audio=True).order_by("abr").last()
        return yt, mp4_files
    except Exception as e:
        print(e)
        return None, None