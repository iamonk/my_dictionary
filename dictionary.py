# Importing Stuff
import secret
import requests as requests



#word=input("Enter Word to be searched:  ")
word="Desire"

#Final url
final_url=f"{secret.url}{word}?key={secret.dict_api_key}"


#Fetching Data
r = requests.get(final_url)
r=r.json()
#meta=r['meta']['id']
#print(meta)
print(type(r))

defi=r[0]['shortdef']
for d in defi:
    print("\n",d)

