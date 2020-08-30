# CMU Graphics Framework taken from 15-112 Course: Fundamentals of Programming and Computer Science
# https://www.kosbie.net/cmu/fall-19/15-112/notes/notes-animations-part2.html
from cmu_112_graphics import *

#external files
from appScreens import *
from Market_Hedges import *



# App Framework taken from Carnegie Mellon 15-112 Course: Fundamentals of Programming and Computer Science
# link: https://www.kosbie.net/cmu/fall-19/15-112/notes/notes-animations-part2.html
class CorrelationApp(ModalApp):
    def appStarted(app):
        app.splashScreen = splashScreen()
        app.helpScreen = helpScreen()
        app.loadScreen = loadScreen()
        app.correlationTable = correlationTable()
        app.learnScreen = learnScreen()
        app.setActiveMode(app.splashScreen)

CorrelationApp(width=850, height=600)

