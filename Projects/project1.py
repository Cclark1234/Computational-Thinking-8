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

s1 = codesters.Sprite("basketball",100,100)
s1.set_size(1.5)

s2 = codesters.Sprite("hoop",-100,-100)
s2.set_size(1.0)

s3 = codesters.Sprite("cardinal",100,-100)
s3.set_size(0.5)

s4 = codesters.Sprite("rod wave",-100,100)
s4.set_size(0.5)

message1 = codesters.Text("Christian Clark",0,220,"red")
message2 = codesters.Text("Ball Is Life",0,-220,"DarkSlateBlue")