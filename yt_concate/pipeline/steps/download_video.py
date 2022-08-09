from yt_concate.pipeline.steps.step import Step
from pytube import YouTube
from yt_concate.pipeline.settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])
        for yt in yt_set:
            if utils.video_file_exists(yt):
                print(f'found existing video file for {yt.url}, skipping')
                continue
            print('downloading', yt.url)
            YouTube(yt.url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id + '.mp4')

        return data
