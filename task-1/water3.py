def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4

def successors(s):
    x, y, z = s
    t = 8 - x
    if t > 0 and y > 0:
	if y > t:
		yield((8,y-t,z),t)
    
