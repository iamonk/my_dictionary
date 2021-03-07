# Importing Stuff
import secret
import sub_direc_rule as sb
import requests as requests
import time



#word=input("Enter Word to be searched:  ")
word="3-D"


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
print(sub_dir_l)

audio_url=f"{secret.audio_url}{sub_dir_l[0]}/{sound[0]}.mp3"


# audio_url=f"{secret.audio_url}" 
# audio=r[1]
# print(audio)