import turtle as trtl 
trtl.pendown()
# draw slinky of 6 circles
for i in range(6):
  trtl.circle(20)
  trtl.penup()
  trtl.forward(20)
  trtl.pendown()
'''
draw x-y axes 100 pixels long each
going in each direction
 '''' 
def draw_axes():
  # centers origin
  trtl.goto(0,0)
  trtl.pendown()
  #draws y axis
  trtl.forward(100)
  trtl.backward(200)
  trtl.forward(100)
  trtl.left(90)
  #draws x axis
  trtl.forward(100)
  trtl.backward(200)
  trtl.pendown()
  trtl.goto(0,0)

draw_axes()
