from yt_concate.pipeline.steps.step import Step
import ast

class ReadCaption(Step):
    def process(self, data, inputs, utils):
        for yt in data:
            if not utils.caption_file_exists(yt):
                continue

            captions = {}
            with open (yt.caption_filepath ,'r' ) as f:
                for line in f:
                    dic = ast.literal_eval(line)
                    caption = dic["text"]
                    starttime = dic["start"]
                    duration = dic["duration"]
                    video_time = [starttime, duration]
                    captions[caption] = video_time

            yt.captions = captions

        return data

