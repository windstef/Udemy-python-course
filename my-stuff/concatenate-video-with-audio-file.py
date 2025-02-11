# How to Combine an Audio and Video File With 7 Lines of Python
# https://jacobnarayan.com/blogs/how-to-combine-an-audio-and-video-file-with-7-lines-of-python

import os
import sys
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# Get the desired video title
title = input("Enter a title: ")
# Now we’ll open the video and audio files that we want to combine. We’ll use VideoFileClip and AudioFileClip to open the files.

# Open the video and audio
# video_clip = VideoFileClip("video.mp4")
# audio_clip = AudioFileClip("audio.mp3")
# Once we have opened the clips, we can combine them using concatenate_videoclips. This will combine the video clip with the audio clip to create a single clip with both elements.

# Use the already existed, downloaded, video and audio files from youtube
video_clip = VideoFileClip("Χάρτες Κτηματολογίου. πως να βρείτε και να εκτυπώσετε το χωράφι σας - 720p - no audio.mp4")
audio_clip = AudioFileClip("audio/Χάρτες Κτηματολογίου. πως να βρείτε και να εκτυπώσετε το χωράφι σας.mp3")

# Concatenate the video clip with the audio clip

final_clip = video_clip.set_audio(audio_clip)
# Finally, we can use write_videofile to export the finished video with audio as an .mp4 file. The title that was entered earlier will be used as the file name for easy identification.

# Export the final video with audio
final_clip.write_videofile(title + ".mp4")