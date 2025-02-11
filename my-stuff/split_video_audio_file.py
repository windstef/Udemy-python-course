import os
import sys
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip

# https://medium.com/@henryreith/split-your-video-files-into-x-second-parts-for-instagram-friendly-segments-using-python-ea0f7fd1dad0
# This article will introduce a simple yet efficient Python script that can automatically split your video files into segments of any desired length. In our case, we’ll be splitting videos into Instagram-friendly lengths, like 59 seconds or even 14 seconds for Instagram Stories.

def split_video(filename, segment_length, output_dir):
    clip = VideoFileClip(filename)
    duration = clip.duration

    start_time = 0
    end_time = segment_length
    i = 1

    # Extract the filename without extension
    basename = os.path.basename(filename).split('.')[0]

    # Extract directory path
    dir_path = os.path.dirname(filename)

    output_path = os.path.join(dir_path, output_dir)

    # Create output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    while start_time < duration:
        output = os.path.join(output_path, f"{basename}_part{i}.mp4")
        ffmpeg_extract_subclip(filename, start_time, min(end_time, duration), targetname=output)
        start_time = end_time
        end_time += segment_length
        i += 1
    print(f'Video split into {i-1} parts.')


# try with the video file:
# Χάρτες Κτηματολογίου. πως να βρείτε και να εκτυπώσετε το χωράφι σας - 720p - no audio.mp4
if __name__ == "__main__":
    # video_path = sys.argv[1]  # first argument from command line
    video_path = "Χάρτες Κτηματολογίου. πως να βρείτε και να εκτυπώσετε το χωράφι σας - 720p - no audio.mp4"
    # segment_length = int(sys.argv[2])  # second argument from command line
    segment_length = 600

    # output_dir = sys.argv[3]  # third argument from command line
    output_dir = "/home/stefkour/PycharmProjects/app1/pythonProject/my-stuff/video"
    split_video(video_path, segment_length, output_dir)