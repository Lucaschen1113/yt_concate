import time
import json

from youtube_transcript_api import YouTubeTranscriptApi
from .step import Step

from .step import StepException


class DownloadCaptions(Step):

    def process(self, data, inputs, utils):
        for yt in data:
            if utils.caption_file_exists(yt):
                continue
            #video_id = utils.get_video_id_from_url(yt.url)
            try:
                captions = YouTubeTranscriptApi.get_transcript(yt.id)
                time.sleep(1)
                captions_l = list(json.dumps(i) for i in captions)
                with open(yt.caption_filepath, 'w', encoding='utf-8') as fp:
                    for i in captions_l:
                        fp.write(i + '\n')
            except:
                print('Subtitle is disabled for video id:', yt.url)

        return data
