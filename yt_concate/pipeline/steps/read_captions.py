import os
import ast
from pprint import pprint

from yt_concate.pipeline.steps.step import Step
from yt_concate.pipeline.settings import CAPTIONS_DIR


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        data = {}
        for caption_file in os.listdir(CAPTIONS_DIR):
            captions = {}
            with open (os.path.join(CAPTIONS_DIR,caption_file) ,'r' ) as f:
                for line in f:
                    dic = ast.literal_eval(line)
                    caption = dic["text"]
                    starttime = dic["start"]
                    captions[caption] = starttime

                data[caption_file] = captions

        pprint(data)
        return data

