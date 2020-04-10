import pyyoutube
import json
import matplotlib.pyplot as plt

# Set API Key and PlayList ID
with open("api_key.dat") as fin:
    api_key = fin.read().strip()
playlist_id = "PLsLWHLZB96VeVp3IVzvSH58ttVz_Anr7H"

api = pyyoutube.Api(api_key=api_key)
playlist_item_by_playlist = api.get_playlist_items(playlist_id=playlist_id, count=10) # Set count=None to get all videos of the playlist

video_names = []
video_stats = []

for item in playlist_item_by_playlist.items:
    video_id = item.snippet.resourceId.videoId
    video = api.get_video_by_id(video_id=video_id).items[0]
    video_names.append(video.snippet.title)
    video_stats.append(int(video.statistics.viewCount))
 
fig, ax = plt.subplots()
y_pos = range(len(video_names))
video_stats, video_names = zip(*sorted(zip(video_stats, video_names), reverse=True))

ax.barh(y_pos, video_stats)
ax.set_yticks(y_pos)
ax.set_yticklabels(video_names)
ax.invert_yaxis() 
ax.set_xlabel('View Count')
ax.set_title('Top Watched Videos')

#plt.show()
plt.savefig("list.pdf", bbox_inches='tight')
