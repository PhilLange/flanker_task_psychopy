import random
from constants import *
from psychopy.visual import TextStim, Window
from psychopy.event import waitKeys
from psychopy.sound import Sound
from psychopy import core
disp = Window(DISPSIZE, units='pix', fullscr=True)
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
#boomer = Sound(value='peter-kuli-jedwill-ok-boomer-official-music-video-mp3cut (online-audio-converter.com).wav')
letter = random.choice(vowels)
vowelstim = TextStim(disp, text=letter, height=128)
high = Sound(secs=0.5, value=4000)
low  = Sound(secs=0.5, value=400)

vowelstim.draw()
disp.flip()

# wait for response
resplist = waitKeys(maxWait=float('inf'), keyList=vowels,
                    timeStamped=True)

# select first response from the list
key, presstime = resplist[0]
if key == letter:
    correct = 1
else:
    correct = 0
if correct:
    high.play()
    feedback = 'Gut gemacht!'
    fbcolor = (-1, -1, -1)
else:
    low.play()
    feedback = 'Falsch!'
    fbcolor = (-1, -1, -1)


fbstim    = TextStim(disp, text=feedback, color=fbcolor,
                     height=24)
fbstim.draw()
disp.flip()
core.wait(secs=1)
extrafb = 'Der Buchstabe war %s und deine Antwort war %s.' % (letter, key)
extrafbpos = (0, int(DISPSIZE[1] * -0.1))
extrafbstim = TextStim(disp, text=extrafb, pos=extrafbpos,
                       height=128)
extrafbstim.draw()
disp.flip()
waitKeys(maxWait=float('inf'), keyList=None)
disp.close()
