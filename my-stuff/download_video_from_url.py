# download video from web url


# guidelines
# https://stackoverflow.com/questions/30953104/download-video-from-url-in-python
# https://github.com/ankitjain28may/pythonResources/blob/master/Download%20video%20from%20cmd%20using%20python/run.py

# case 1 (eltube):
# https://www.eltube.gr/watch.php?vid=271cf5638
# HTTP Error 403: Forbidden


# case 2 (youtube)
# https://www.youtube.com/watch?v=lBnsmQbAkY4
# downloaded only 945 kB

#########################
# 1st script

# import urllib.request
# url = input("Enter the Youtube-url\n")
# name = input("Enter the name for the video\n")
# name=name+".mp4"
# try:
#     print("Downloading starts...\n")
#     urllib.request.urlretrieve(url, name)
#     print("Download completed..!!")
# except Exception as e:
#     print(e)



################################################
# 2nd script

# pip install smart_open[http]
# from smart_open import open
#
# def stream_uri(uri_in, uri_out, chunk_size=1 << 18):  # 256kB chunks
#     """Write from uri_in to uri_out with minimal memory footprint."""
#     with open(uri_in, "rb") as fin, open(uri_out, "wb") as fout:
#         while chunk := fin.read(chunk_size):
#             fout.write(chunk)

# from https to disk

# url = "https://ik.imagekit.io/demo/sample-video.mp4"
# stream_uri(url, "./sample-video.mp4")    # ok

# url ="https://www.youtube.com/watch?v=lBnsmQbAkY4"
# stream_uri(url, "./youtube-video.mp4")    # only 910 kB


# url ="https://www.eltube.gr/watch.php?vid=271cf5638"
# stream_uri(url, "./eltube-video.mp4")    # only 118 kB


# from s3 to ftp
# stream_uri("s3://bucket1/example.pdf", "ftp://192.168.178.1:21/example.pdf")


################################################
# 3rd script
# pip install pytube

from pytube import YouTube

# def Download(link):
#     try:
#         youtubeObject = YouTube(link)
#         youtubeObject = youtubeObject.streams.get_highest_resolution()
#         youtubeObject.download()
#         print("Download is completed successfully")
#     except Exception as e:
#         print("An error has occurred")
#         print(e)
#
#
# link = input("Enter the YouTube video URL: ")
# Download(link)

# try with youtube video link:
# https://www.youtube.com/watch?v=lBnsmQbAkY4
# result:
# An error has occurred
# HTTP Error 400: Bad Request

# https://www.eltube.gr/watch.php?vid=271cf5638
# result:
# An error has occurred
# regex_search: could not find match for (?:v=|\/)([0-9A-Za-z_-]{11}).*



################################################
# 4th script
# pip install pytube

# https://handhikayp.medium.com/download-youtube-video-and-audio-using-python-dd47ca2fb060

# from pytube import YouTube
#
# urls =  input("url:")
#
# vid = YouTube(urls)
#
# video_download = vid.streams.get_highest_resolution()
# # video_download = vid.streams.get_lowest_resolution()
#
# audio_download = vid.streams.get_audio_only()
#
# entry = YouTube(urls).title
#
# print(f"\nVideo found: {entry}\n")
#
# print(f"Downloading Video...")
# video_download.download(filename=f"{entry}.mp4")
#
# print("Downloading Audio...")
# audio_download.download(filename=f"{entry}.mp3")
#
# print("Program Completed")

# try with youtube video link:
# https://www.youtube.com/watch?v=lBnsmQbAkY4
# result:
# urllib.error.HTTPError: HTTP Error 400: Bad Request

# search:
# https://stackoverflow.com/questions/78160027/how-to-solve-http-error-400-bad-request-in-pytube


################################################
# 5th script
# pip install pytubefix

# Note:
# https://stackoverflow.com/questions/78160027/how-to-solve-http-error-400-bad-request-in-pytube
# https://github.com/pytube/pytube/issues/1947


from pytubefix import YouTube
from pytubefix.cli import on_progress
from setuptools.errors import ExecError

url =  input("url:")

try:
    print("Download starts: ")
    yt = YouTube(url, on_progress_callback=on_progress)

    print(yt.title)
    # print(yt.vid_info())

    # ys = yt.streams.get_highest_resolution()     # video + audio at 360p
    # ys.download()

    # ys = yt.streams.get_by_resolution("720p")

    # ys = yt.streams.filter(resolution="720p").first().download()      # downloaded at 720p but no audio

    # ys = yt.streams.get_highest_resolution(False)      # downloaded at 720p but no audio
    # ys.download()

    audio = yt.streams.get_audio_only()
    audio.download('audio')     # dir: audio mp4


    print("Download finished.")
except Exception as e:
    print("Error has occurred:")
    print(e)


# works for in 360p resolution:
# https://www.youtube.com/watch?v=lBnsmQbAkY4


