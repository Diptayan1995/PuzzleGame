from MediumRoom import MediumRoom
class DifficultRoom(object):
    def difficult_room(self):
	g= MediumRoom(0)
	answer_count=0
	m=g.medium_room()
	if int(m)==2:
	    print "In a group of three people A , B and C , one of them always tells the truth."
	    print "One always lies and one alternates between truth and lie ."
	    print "One of them is a psychologist , the other one is a pediatrician."
	    print "And the third one is a physiotherapist , in no particular order."
	    print "When interrogated .... "
	    print "B says : I am the psychologist . C is a physiotherapist."
            print "A says : I am the psychologist . B is a pediatrician."
	    print "C says : A is the pediatrician . B is a psychologist."
	    print "\n"
	    print "So who is the person that alternates between truth and lie?"
	    if str(raw_input("> ")).upper()=="B":
	        answer_count=answer_count+1
	    print "\n"			
            print "And who among the three is the pediatrician?"
	    if str(raw_input("> ")).upper()=="B":
		answer_count=answer_count+1
            print "\n"
	    print "And tell me who is the person who always lies?"
	    if str(raw_input("> ")).upper()=="C":
		answer_count=answer_count+1
	    if answer_count==3:
		print "you got all of them right :)"
		print "you cleared all 3 levels. You are a genius"
	    else:
		print "you gave %r right answer/answers from Difficult Room." % answer_count
		print "you only cleared level ",m
		print "you failed at level 3 . Try again and see if you can do it."
	elif int(m)==0:
	    print "Game Over."
	    print "you couldn't clear any level"
            print "You know nothing."
	elif int(m)==1:
	    print "Game Over."
	    print "you only cleared level ",m
	    print "you can do better."
f=DifficultRoom()
f.difficult_room()
