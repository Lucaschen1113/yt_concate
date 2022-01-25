import time
import json

from youtube_transcript_api import YouTubeTranscriptApi

from .step import Step
from .step import StepException


class DownloadCaptions(Step):

    def process(self, data, inputs, utils):
        for url in data:
            if utils.caption_file_exists(url):
                continue
            video_id = utils.get_video_id_from_url(url)
            try:
                captions = YouTubeTranscriptApi.get_transcript(video_id)
                time.sleep(1)
                captions_l = list(json.dumps(i) for i in captions)
                with open(utils.get_caption_filepath(url), 'w', encoding='utf-8') as fp:
                    for i in captions_l:
                        fp.write(i + '\n')
            except:
                print('Subtitle is disabled for video id:', video_id)
