## the following line is just MAGIC ##############################################
## we need it to be able to draw images on the screen ############################
from medialib import *
initialize() # always the first instruction of the program
##################################################################################
clear(0,0,255)
draw("images/cake.png",100,150)
draw("images/cake2.png",180,155)
text("Example 2",10,10,16)
text("Click the left button on the mouse to continue...",10,500,16)
wait_mouse_leftclick()

all_done() # always the last instruction of the program