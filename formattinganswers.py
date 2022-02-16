filename = "P101 Fun Trivia Answers.txt"
with open(filename, 'r',encoding="utf8") as myfile:

    lines = myfile.readlines()

counter = 0
dict = {" ":" "}
key = ""
value = ""
for line in lines:
    if(counter == 0):
        key = line[:-1]
        counter=1
        print("key",key)
    else:
        value = line[8:-1]
        counter = 0
        print("value",value)
        dict.update({key:value})

import json

from numpy import save
  
savefile = filename[5:-12]
savefile = "Pirate101 "+savefile+".json"
  
with open(savefile, "w") as outfile:
    json.dump(dict, outfile)
