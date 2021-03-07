# Importing Stuff
import secret
import requests as requests



#word=input("Enter Word to be searched:  ")
word="pajama"


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
print(sound)


# audio_url=f"{secret.audio_url}" 
# audio=r[1]
# print(audio)