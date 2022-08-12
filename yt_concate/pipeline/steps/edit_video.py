from yt_concate.pipeline.steps.step import Step
from moviepy.editor import VideoFileClip, concatenate_videoclips


class EditVideos(Step):
    def process(self, data, inputs, utils):
        clips = []
        for found in data:
            # print(found.time[0])
            start = found.time[0]
            duration = found.time[1]
            video = VideoFileClip(found.yt.video_filepath).subclip(int(start), int(start + duration))
            clips.append(video)
            if len(clips) >= inputs['limits']:
                break
        print(clips)

        final_clip = concatenate_videoclips(clips)
        output_filepath = utils.get_output_filepath(inputs['channel_id'], inputs['search_word'])
        final_clip.write_videofile(output_filepath, codec='libx264')

