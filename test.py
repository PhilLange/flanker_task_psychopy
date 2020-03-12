from psychopy import visual, core
from constants import DISPSIZE, fixCrossSize

disp = visual.Window(size=DISPSIZE, units='pix', fullscr=False)

fixmark = visual.ShapeStim(disp, lineColor='#000000', lineWidth=3.0,  # fixation cross
                           vertices=((-fixCrossSize / 2, 0), (fixCrossSize / 2, 0), (0, 0),
                                     (0, fixCrossSize / 2), (0, -fixCrossSize / 2)),
                           units='pix', closeShape=False)

lf = visual.ImageStim(disp, image="flankerL.bmp", name='flankerL')
ri = visual.ImageStim(disp, image='target_R_I.bmp', name='rightIncongruent')

fixmark.draw()
disp.flip()
core.wait(1)
lf.draw()
disp.flip()
core.wait(1)
ri.draw()
disp.flip()
core.wait(1)
disp.close()
