# Importing Stuff
import secret
import requests as requests

# Getting Words
word=input("Enter Word to be searched:  ")

#Final url
final_url=f"{secret.url}{word}?key={secret.dict_api_key}"
print("\n",final_url)

#Fetching Data

response = requests.get(final_url)
print("\n",response)

