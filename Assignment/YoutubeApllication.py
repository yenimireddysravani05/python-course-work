video_id = 1025
video_title = "Learning Python in 30 Minutes"
duration = 30.00
tags = ["Python", "Tutorial", "Beginner", "Programming"]
metrics = (105000, 9800)  
like_ratio = 93.3 
features = {"HD", "Subtitles", "No Ads"}
channel_info = {
    "name": "CodeWithSrav",
    "email": "support@srav.com",
    "location": "Hyd"
}
print("\n" + "="*65)
print("="*65)
print("Video ID, Title, Duration:", video_id, video_title, str(duration).replace('.', ','), sep=',')
print("Like Ratio: %.2f%%" % like_ratio)
print(f"Title: {video_title}")
print(f"Duration: {duration} minutes")
print(f"Views: {metrics[0]}")
print(f"Likes: {metrics[1]}")
print(f"Tags: {tags[0]}, {tags[1]}, {tags[2]}, {tags[3]}")
print(f"Features: {', '.join(features)}")
print("Channel Info: {}, Email: {}, Location: {}".format(
    channel_info["name"],
    channel_info["email"],
    channel_info["location"]
))
print("Formatted Video ID:", str(video_id).zfill(6))
print("Title (centered, 40 chars):".center(40, "="))
print(video_title.center(40))
print("Channel Location (left):", channel_info["location"].ljust(20, '.'))
print("Channel Email (right):", channel_info["email"].rjust(30, '*'))
print("Tag 1:", tags[0])
print("Tag 2:", tags[1])
print("Tag 3:", tags[2])
print("Tag 4:", tags[3])
like_percent = (metrics[1] / metrics[0]) * 100
print("Like %: {:.1f}%".format(like_percent))
print("Channel: {name} | City: {location}".format(**channel_info))
print("------------------------------ VIDEO SUMMARY------------------------------------")
print(f"Title: {video_title}")
print(f"Video_ID: {str(video_id).zfill(6)}")
print(f"Duration: {duration:.2f} minutes")
print(f"Tags: {tags[0]}, {tags[1]}, {tags[2]}, {tags[3]}")
print(f"Features: {', '.join(features)}")
print(f"Views: {metrics[0]}")
print(f"Likes: {metrics[1]} ({like_percent:.1f}%)")
print(f"Like_Ratio: {like_ratio:.2f}%")
print(f"Channel: {channel_info['name']}")
print(f"Contact: {channel_info['email']}, {channel_info['location']}")
print("----------------------------------------------------------------------------------")