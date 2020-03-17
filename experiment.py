from psychopy import core, visual, event
from psychopy.tools.filetools import fromFile, toFile
import time, numpy as np
from constants import DISPSIZE, fixCrossSize
import os

# Initialise a new Window instance.
disp = visual.Window(size=DISPSIZE, units='pix', fullscr=True)

# creating stimuli
fixmark = visual.ShapeStim(disp, lineColor='#000000', lineWidth=3.0,                           # fixation cross
                           vertices=((-fixCrossSize / 2, 0), (fixCrossSize / 2, 0), (0, 0),
                                     (0, fixCrossSize / 2), (0, -fixCrossSize / 2)),
                           units='pix', closeShape=False)
lf = visual.ImageStim(disp, image="flankerL.bmp", name='flankerL')                             # left flanker
rf = visual.ImageStim(disp, image="flankerR.bmp", name='flankerR')                             # right flanker
li = visual.ImageStim(disp, image='target_L_I.bmp', name='leftIncongruent')                    # Left Incongruent
lc = visual.ImageStim(disp, image='target_L_C.bmp', name='leftCongruent')                      # Left Congruent
ri = visual.ImageStim(disp, image='target_R_I.bmp', name='rightIncongruent')                   # Right Incongruent
rc = visual.ImageStim(disp, image='target_R_C.bmp', name='rightCongruent')                     # Right Congruent

stims = [lf, rf, li, lc, ri, rc]

# Draw the fixmark stimulus and flip to screen
fixmark.draw()
disp.flip()
core.wait(1)
lf.draw()
disp.flip()
core.wait(1)
ri.draw()
disp.flip()
core.wait(1)

# close screen to prevent freezing
disp.close()
