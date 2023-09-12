def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4

def successors(s):
    x, y, z = s
    tf = 8 - x
    if (tf > 0) and (y > 0):
	    if y > tf:
		    yield((8,y-tf,z),tf)
	    else:
		    yield((x+y,0,z),y)
    if (tf > 0) and (z > 0):
	    if z > tf:
		    yield((8,y,z-t),tf)
	    else:
		    yield((x+z,y,0),z)
    ts = 5 - y
    if (ts > 0) and (x > 0):
	    if x > ts:
		    yield((x-ts,5,z),ts)
	    else:
		    yield((0,y+x,z),x)
    if (ts > 0) and (z > 0):
	     if z > ts:
		     yield((x,5,z-ts),ts)
	     else:
		     yield((x,y+z,0),z)
    tt = 3 - z
    if (tt > 0) and (x > 0):
	     if x > tt:
		     yield((x-tt,y,3),tt)
	     else:
		     yield((0,y,z+x),x)
    if (tt > 0) and (y > 0):
	     if y > tt:
		     yield((x,y-tt,3),tt)
	     else:
		     yield((x,0,z+y),y)
    
