from psychopy import core, visual, gui, data, event, sound, logging
from psychopy.tools.filetools import fromFile, toFile
import time, numpy as np
from constants import DISPSIZE, fixCrossSize
from gui import gui_flanker

# subject information
gui_flanker()
# Initialise a new Window instance.
disp = visual.Window(size=DISPSIZE, units='pix', fullscr=True)

# fixation cross
fixmark = visual.ShapeStim(disp, lineColor='#000000', lineWidth=3.0,
                           vertices=((-fixCrossSize / 2, 0), (fixCrossSize / 2, 0), (0, 0),
                                     (0, fixCrossSize / 2), (0, -fixCrossSize / 2)),
                           units='pix', closeShape=False)
# Draw the fixmark stimulus and flip to screen
fixmark.draw()
disp.flip()
core.wait(2)
# close screen to prevent freezing
disp.close()
