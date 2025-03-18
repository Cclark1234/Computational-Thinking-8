###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("brickwall")
mySprite = codesters.Sprite("rod wave")
mySprite.set_size(0.5) 
mySprite.say("Christian Clark!")


print("\t3: a few icons should appear - click the globe")
print("\t4: a new tab will open - click CONNECT")
print("\n\nWhen you have found the CARDINAL, click here, then use CTRL C to end the program\n\n")