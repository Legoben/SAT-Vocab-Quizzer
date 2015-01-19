import random
import time
#import pynotify
import rumps
import sys
import webbrowser


#def sendmessage(title, message):
#    pynotify.init("Test")
#    notice = pynotify.Notification(title, message)
#    notice.show()
#    return


def doWords(arg):
	print("here")
	
	
	tchoice = random.choice(wdef)
	rumps.notification("SAT Word", "", "What does the word " + tchoice['word'] + " mean?")
	time.sleep(6)	
	rumps.notification(tchoice['word'] + " means:", "",tchoice['def'])
	print(tchoice['word'] + " means:",tchoice['def'])
	
	if timer.interval != 300:
		timer.interval = 300
		print("Change int")
	
	


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


txtarry = open("words.txt").read().split("\n")
#print txtarry

wdef = []

for word in txtarry:
	warry = word.split(" ")
	tword = warry[0].strip()
	defintion = word.lstrip(tword).strip()
	#print(tword)
	#print(defintion)
	wdef.append({"word":tword,"def":defintion})


@rumps.clicked("View Source")
def open_github(_):
	webbrowser.open_new_tab("https://github.com/Legoben/SAT-Vocab-Quizzer")
	pass


@rumps.clicked('Quit')
def do_quit(_):
    rumps.quit_application()
    sys.exit()
    
	

app = rumps.App('SAT Words', quit_button=None)
timer = rumps.Timer(doWords, 40)
timer.start()
app.run()

