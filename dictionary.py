# Importing Stuff
import secret
import sub_direc_rule as sb
import requests as requests
import time
import vlc 
from playsound import playsound



#word=input("Enter Word to be searched:  ")
word="prejudice"


#Final url
final_url=f"{secret.url}{word}?key={secret.dict_api_key}"


#Fetching and converting Data
r = requests.get(final_url).json()

#Short Defination
defi=r[0]['shortdef']
for d in defi:
    print("\n",d)


#Audio

pron_list=r[0]['hwi']['prs']
sound=[x['sound']['audio'] for x in pron_list]

sub_dir_l=sb.sub_dir(sound)
# print(sub_dir_l)

audio_url=f"{secret.audio_url}{sub_dir_l[0]}/{sound[0]}.mp3"

with requests.get(audio_url) as rq:
    with open('audio.mp3','wb') as file:
        file.write(rq.content)

playsound('audio.mp3')

# p=vlc.MediaPlayer(audio_url)
# p.play()



# audio_url=f"{secret.audio_url}" 
# audio=r[1]
# print(audio)