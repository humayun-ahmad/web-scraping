# import module
from pytube import YouTube

# Save path
save_path = "C:/Users\acer\Desktop\web-scraping\Youtube_video_download" 

# download link
link = "https://youtu.be/32dX-HPIyRk?list=PLgH5QX0i9K3oWTwTgILA7v9oysoDgkJDg"



try:
    video_obj = YouTube(link)
except:
    print("connection problem, check your connection status")
    

video_obj.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1]

print(video_obj)
# mp4file = video_obj.filter("mp4")

# video_obj.set_filename("demo_video")

# # set video extention and resolution

# ER_video = video_obj.get(mp4file[-1].extention, mp4file[-1].resolution)



try:
    # video download start from here
    video_obj.download()
except:
    print("some error are happend above customization please check you code...")

print("video download completee!")







