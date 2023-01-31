# Import YouTube class:
from pytube import YouTube

# let’s try to download a video
# let's try to download Gangnam style - PSY
yt = YouTube('https://www.youtube.com/watch?v=9bZkp7q19f0')

# For advanced use cases, you can provide some additional arguments when you create a YouTube object:
# yt = YouTube(
#   'https://www.youtube.com/watch?v=9bZkp7q19f0',
#   on_progress_callback=progress_func,
#   on_complete_callback=complete_func,
#   proxies=my_proxies,
#   use_oauth=False,
#   allow_oauth_cache=True
# )



# Now, we have a YouTube object called yt

# Get the video Title:
print(yt.title) # PSY - GANGNAM STYLE(강남스타일) M/V

# And this would be how you would get the thumbnail url:
print(yt.thumbnail_url) # https://i.ytimg.com/vi/9bZkp7q19f0/sddefault.jpg

# WORKING WITH STREAM
# There are two technics for streaming : DASH (Dynamic Adaptative Streaming over HTTP) and Progressive stream
# You can choose one of the two methods by using .filter(args)
# For DASH:
yt.streams.filter(adaptive=True)

# For Progressive:
# yt.streams.filter(progressive=True)

# Filtering for audio-only:
# yt.streams.filter(only_audio=True)

# Filtering for MP4 Streams:
yt.streams.filter(file_extension='mp4')

# downloading Streams:
stream = yt.streams.get_by_itag(22) # you can see itag from the filter results
stream.download() # progressive and DASH


