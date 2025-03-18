###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background("summer")

q1 = codesters.Square(100,100,200, 'black')
q2 = codesters.Square(-100,100,200, 'blue')
q3 = codesters.Square(-100,-100,200, 'red')
q4 = codesters.Square(100,-100,200, 'white')