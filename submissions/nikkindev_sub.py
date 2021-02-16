# pip install PyDictionary

from PyDictionary import PyDictionary
import random

dic=PyDictionary()

challenge = '3 of those who writes me a haiku in python, and its doing at least something, will get 3 ceth each, but only TOP 3!!'

challenge_words = challenge.split() 
challenge_words = [word.strip(',') for word in challenge_words]
challenge_words = [word.strip('!') for word in challenge_words]
its_haiku_time = True
haiku = []

while its_haiku_time:
  haiku_words = dic.synonym(random.choice(challenge_words))
  if (haiku_words != None):
    haiku_word = random.choice(haiku_words)
    if(len(haiku_word.split()) != 1 or haiku_word in haiku): continue
    haiku.append(haiku_word)
  if (len(haiku) == 13):
    break

print('Here\'s the Haiku:')
print(' ',' '.join(haiku[0:4]),'\n ',' '.join(haiku[4:9]),'\n ',' '.join(haiku[9:13]))
