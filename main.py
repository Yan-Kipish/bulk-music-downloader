"""
pip install pytube
Get ffmpeg on https://www.ffmpeg.org/download.html
Path to ffmpeg binary should be set in "ffmpeg_cmd" variable
Make "videos" and "audio" folders nearby the script
"""

import os
import subprocess
import pytube


def download_videos_from_playlist(playlist_url, videos_path):
    playlist = pytube.Playlist(playlist_url)
    for video in playlist.videos:
        download_single_video(video, videos_path)


def download_single_video(video, output_path):
    video.streams.filter(file_extension='mp4').first() \
        .download(output_path=output_path)
    print(f"{video.title} downloaded")


def convert_videos_to_mp3(video_name):
    ffmpeg_cmd = 'C:\\projects\\ffmpeg-4.4-full_build\\bin\\ffmpeg.exe'
    video_abspath = os.path.join(os.curdir, "videos") + "\\" + video_name
    audio_abspath = os.path.join(os.curdir, "audio") + "\\" + video_name.split('.')[0] + ".mp3"
    subprocess.call([ffmpeg_cmd, '-i', video_abspath, audio_abspath])


def clean_video_folder(videos_path):
    [
        os.remove(fr"{videos_path}\{file}")
        for file in os.listdir(videos_path)
        if file.endswith(".mp4")
    ]


def main():
    video_abspath = os.path.join(os.curdir, "videos")
    playlist_url = "https://www.youtube.com/playlist?list=YOUR_PLAYLIST_URL"
    download_videos_from_playlist(playlist_url, video_abspath)
    for video_name in os.listdir(video_abspath):
        convert_videos_to_mp3(video_name)
    clean_video_folder(video_abspath)


if __name__ == '__main__':
    main()
