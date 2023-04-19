from gtts import gTTS 
import os
import time
run=True
while(run):
    start_word="ALEXA. "
    input="A"
    if(input=="J"):
        command = "TELL ME A JOKE"
    elif(input=="W"):
        command = "WHAT IS THE WEATHER LIKE TODAY?"
    else:
        command = "SAY SOMETHING" #DEFAULT CASE
    text=start_word + command
    language = 'en'
    speech = gTTS(text=text,lang=language,slow=False)

    speech.save("text.mp3")
    os.system("start text.mp3")
    time.sleep(10)

'''
A - 
'''