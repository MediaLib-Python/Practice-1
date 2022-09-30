## the following line is just MAGIC ##############################################
## we need it to be able to draw images on the screen ############################
from medialib import *
initialize() # always the first instruction of the program
##################################################################################

draw("eye.png",100,100)
draw("eye2.png",100+50,100)
print("Click the left button on the mouse to continue...") 
#try to change print() to text()and see what happens 

wait_mouse_leftclick()




#Move both eye.png and eye2.png 100 downwards first,
#pause the control flow of the program until the mouse's left button is pressed. 





#Move both eye.png and eye2.png 50 going towards the right,
#pause the control flow of the program until the mouse's left button is pressed. 



print("done")

all_done() # always the last instruction of the program

##use variables to make the code more readable

## try to define a function yourself to further improve the readability of the previous code




