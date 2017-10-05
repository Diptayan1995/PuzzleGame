from EasyRoom import EasyRoom
class MediumRoom(object):
    def __init__(self,count):
        self.count=count
    def medium_room(self):		
	t= EasyRoom(self.count)
	d=t.easy_room()
	if int(d)==0:
	    return d
	elif int(d)==1:
	    print "1 , 11 , 21 , 1211 , 111221 , 312211 , 13112221 , 1113213211 , 31131211131221 , ....."
	    print "What is the next number of the sequence?? "
	    if (raw_input("> "))==str(13211311123113112211):
		print "\n"
		print "Again you're right!"
		print "\n"
		return (d+1)
	    else:
		print "\n"				
		print "Ouch!.. You're wrong."
		print "\n"
		return d

