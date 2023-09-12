def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4

def successors(s):
    x, y, z = s
    t = 8 - x
    if t > 0 and y > 0:
      	if y>t:
	    yield((8,y-t,z),t)
     	else:
	    yield((x+y,0,z), y)
    if t > 0 and z > 0:
      	if  y>t:
	    yield((8,y,z-t),t)
      	else:
	    yield((x+z,y,0),y)
    
