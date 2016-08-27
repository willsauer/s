import random, urllib2
# mport special libraries already built in python
import random
the_url = "https://raw.githubusercontent.com/bellcodo/congenial-octo-meme/66b0e3c28db56b0abd536f0d9756d0e0f182ea93/activities.lst"
list_raw_text = urllib2.urlopen(the_url).read()
# list of options to select from

possible_activities = ['a', 'b', 'c']
the_url = "raw.githubusercontent.com/bellcodo/congenial-octo-meme"
# choice of what we are going to do
print "debug " + str(list_raw_text.split())
possible_activities = list_raw_text.split()
# display the results to the end user
the_activity = random.choice(possible_activities)
print "Possible activities are: " + str(possible_activities)
print "What we are going to do: " + the_activity
