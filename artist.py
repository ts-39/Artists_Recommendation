import random
import pprint

with open("artist.txt","r")as f:
    artists = f.readlines()
    for i in range(len(artists)):
        artists[i] = artists[i].replace('\n', '')

l = []

for n in range(10):
    random.shuffle(artists)
    l.append(artists[:10])

pprint.pprint(l)