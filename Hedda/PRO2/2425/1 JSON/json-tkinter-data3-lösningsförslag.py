import tkinter as tk
import json

def prettify_time(time):

    # Räknar ut sekunder, minuter, timmar och strängar dem
    seconds = str(time%60)
    minutes = str((time//60)%60)
    hours = str((time//60)//60)

    # Fixa det till tvåsiffriga svar
    if len(seconds) < 2:
        seconds = "0"+seconds
    if len(minutes) < 2:
        minutes = "0"+minutes
    if len(hours) < 2:
        hours = "0"+hours

    return hours+":"+minutes+":"+seconds

with open("data3.json", encoding="utf-8") as f:
    data = json.load(f)

root = tk.Tk()

videos = []
i = 0 # Detta är en fuling...
for key in data:
    if i%2==0:
        color = "#eeeeee"
    else:
        color= "#dddddd"
    i += 1

    new_video = []

    title = data[key]['name']
    length = prettify_time(data[key]['length'])
    views = data[key]['views']
    likes = data[key]['likes']
    dislikes = data[key]['dislikes']
    score = likes-dislikes
    if score > 0:
        score = "+"+str(score)
    else:
        score = str(score)
        
    new_video.append(tk.Label(root, text=title, background=color))
    new_video.append(tk.Label(root, text="Length: "+length, background=color))
    new_video.append(tk.Label(root, text="Views: "+str(views), background=color))
    new_video.append(tk.Label(root, text="Score: "+score, background=color))
    
    videos.append(new_video)
    

for i in range(len(videos)):
    for j in range(len(videos[i])):
        # Den komplicerade formeln gör att datan grupperas snyggt
        videos[i][j].grid(row=(i//3)*4+j, column=i%3,sticky="ewns")
        # Sticky gör att färgerna går ända ut i kanten

        
root.mainloop()
