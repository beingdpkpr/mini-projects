from pytube import YouTube

link = input('Enter the link: ')
# link = 'https://www.youtube.com/watch?v=KiGXn6Gvy1Y'
yt = YouTube(link)

# Title of video
print(f'Title: {yt.title}')
# Number of views of video
print(f'Number of views: {yt.views}')
# Length of the video
print(f'Length of video: {yt.length} seconds')
# Description of video
print(f'Description: {yt.description}')
# Rating
print(f'Rating: {yt.rating}')

# printing all the available streams
# print(yt.streams)

# yt.streams.filter(only_audio=True) - for audio streams
# yt.streams.filter(only_video=True) - for video streams
# Progressive v/s Dash streams. YouTube uses Dash streams for higher-quality rendering.
# print(yt.streams.filter(progressive=True))
# ys = yt.streams.get_by_itag('22') - we can use itag to get any stream

# Get highest resolution streams
ys = yt.streams.get_highest_resolution()

ys.download()
