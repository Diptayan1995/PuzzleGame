class EasyRoom(object):
    def __init__(self, count):
	self.count=count
    def easy_room(self):
	print "At the Pet Show recently I noticed that all except two of the entries were cats."
	print "All except two were dogs."
	print "All except two were fish."
	print "How many of each animal were at the Pet Show?"
	if (raw_input("> "))==str(3):
	    print "Right answer "
	    print "\n"
	    return (self.count+1)
	else:
	    print "Wrong !!!"
	    print "\n"
	    return self.count
			
