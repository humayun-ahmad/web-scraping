# import module
from pytube import YouTube

# Save path
save_path = "C:/Users/acer/Desktop/web-scraping/Youtube_video_download" 

# download link
link = "https://youtu.be/32dX-HPIyRk?list=PLgH5QX0i9K3oWTwTgILA7v9oysoDgkJDg"



try:
    video_obj = YouTube(link)
except:
    print("connection problem, check your connection status")
    

title = video_obj.title

video = video_obj.streams.first()  
video.download(save_path)   

#######################################################################
# The properties of the YouTube object are,
# Title
# Video Id
# Description
# Length
# Thumbnail_URL
# Views
# Rating
# Age Restricted
#######################################################################



print(title)
print(video_obj.video_id)  
print(video_obj.description)  
print(video_obj.length)  
print(video_obj.thumbnail_url)  
print(video_obj.views)  
print(video_obj.rating)  
print(video_obj.age_restricted) 






