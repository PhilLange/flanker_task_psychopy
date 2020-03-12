import random
from constants import *
from psychopy.visual import TextStim, Window
from psychopy.event import waitKeys

disp = Window(DISPSIZE, units='pix', fullscr=True)
vowels = ['a', 'e', 'i', 'o', 'u', 'y']

letter = random.choice(vowels)
vowelstim = TextStim(disp, text=letter, height=128)

vowelstim.draw()
disp.flip()

# wait for response
resplist = waitKeys(maxWait=float('inf'), keyList=vowels,
                    timeStamped=True)

# select first response from the list
key, presstime = resplist[0]

disp.close()