
#112 animation graphics library  from:
#link:https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
from cmu_112_graphics import *
import webbrowser



#used the 112 animation framework for splash screen idea
#link:https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
class splashScreen(Mode):
    def appStarted(mode):
        mode.centerX = mode.width // 2
        mode.centerY = mode.height // 2
        #all images made using canva.com
        mode.background = mode.loadImage("images/relate.png")
        mode.homeButton = mode.loadImage("images/home.png")
        mode.helpButton = mode.loadImage("images/help.png")
        mode.startButton = mode.loadImage("images/start.png")
        mode.learnButton = mode.loadImage("images/learn.png")

        mode.centerHelpX = mode.centerX - mode.centerX/2
        mode.centerStartX = mode.centerX
        mode.centerLearnX = mode.centerX + mode.centerX/2
        mode.buttonY = mode.centerY * 1.5
        mode.buttonWidth = 150
        mode.buttonHeight = 50


    def mousePressed(mode,event):
        x1a,x1b = mode.centerHelpX - mode.buttonWidth/2, mode.centerHelpX + mode.buttonWidth/2
        y1a,y1b = mode.buttonY - mode.buttonHeight/2, mode.buttonY + mode.buttonHeight/2
        x2a, x2b = mode.centerStartX - mode.buttonWidth/2, mode.centerStartX + mode.buttonWidth/2
        y2a, y2b = mode.buttonY - mode.buttonHeight/2, mode.buttonY + mode.buttonHeight/2
        x3a, x3b = mode.centerLearnX - mode.buttonWidth / 2, mode.centerLearnX + mode.buttonWidth / 2
        y3a, y3b = mode.buttonY - mode.buttonHeight / 2, mode.buttonY + mode.buttonHeight / 2

        #line below taken from CMU course website and used throughout code
        # link:https://www.kosbie.net/cmu/fall-19/15-112/notes/notes-animations-part2.html#sidescrollerExamples
        if (x1a <= event.x <= x1b) and (y1a <= event.y <= y1b):
            mode.app.setActiveMode(mode.app.helpScreen)
        if (x2a <= event.x <= x2b) and (y2a <= event.y <= y2b):
            mode.app.setActiveMode(mode.app.loadScreen)
        if (x3a <= event.x <= x3b) and (y3a <= event.y <= y3b):
            mode.app.setActiveMode(mode.app.learnScreen)


    def redrawAll(mode, canvas):
        canvas.create_image(mode.centerX, mode.centerY,
                image=ImageTk.PhotoImage(mode.background))
        canvas.create_image(mode.centerX - mode.centerX/2, mode.buttonY,
                image=ImageTk.PhotoImage(mode.helpButton))
        canvas.create_image(mode.centerX, mode.buttonY,
                image=ImageTk.PhotoImage(mode.startButton))
        canvas.create_image(mode.centerX + mode.centerX / 2, mode.buttonY,
                            image=ImageTk.PhotoImage(mode.learnButton))




#used the 112 animation framework for idea of help screen
#link:https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
class helpScreen(Mode):
    def appStarted(mode):
        #background + dimensions
        mode.about = mode.loadImage("images/about.png")
        mode.centerX = mode.width // 2
        mode.centerY = mode.height // 2

        #images
        mode.homeButton = mode.loadImage("images/home.png")
        mode.homeButton = mode.scaleImage(mode.homeButton, 3/4)
        mode.email = mode.loadImage("images/email.png")
        mode.linkedin = mode.loadImage("images/linkedin.png")
        mode.finvest = mode.loadImage("images/finvest.png")

        #coordinates
        mode.centerHomeX = mode.width/12
        mode.centerHomeY = mode.height/12
        mode.contactY = mode.height*(8.8/10)
        mode.centerEmailX = mode.width/2 - 60
        mode.centerLinkedinX = mode.width/2 + mode.width/5 - 60
        mode.centerFinvestX = mode.width/2 + mode.width/2.5 - 60
        mode.buttonWidth = 150
        mode.buttonHeight = 50

        mode.homeCoordinates = mode.centerHomeX - mode.buttonWidth / 2,\
                          mode.centerHomeY - mode.buttonHeight / 2,\
                          mode.centerHomeX + mode.buttonWidth / 2,\
                          mode.centerHomeY + mode.buttonHeight / 2
        mode.emailCoordinates = mode.centerEmailX - mode.buttonWidth / 2,\
                                mode.contactY - mode.buttonHeight / 2,\
                                mode.centerEmailX + mode.buttonWidth / 2,\
                                mode.contactY + mode.buttonHeight / 2
        mode.linkedinCoordinates = mode.centerLinkedinX - mode.buttonWidth / 2,\
                                   mode.contactY - mode.buttonHeight / 2,\
                                   mode.centerLinkedinX + mode.buttonWidth / 2,\
                                   mode.contactY + mode.buttonHeight / 2
        mode.finvestCoordinates = mode.centerFinvestX - mode.buttonWidth / 2, \
                                  mode.contactY - mode.buttonHeight / 2, \
                                  mode.centerFinvestX + mode.buttonWidth / 2, \
                                  mode.contactY + mode.buttonHeight / 2



    def mousePressed(mode,event):
        #HomeButton
        x1a, y1a, x1b, y1b = mode.homeCoordinates
        if (x1a <= event.x <= x1b) and (y1a <= event.y <= y1b):
            mode.app.setActiveMode(mode.app.splashScreen)


        #email
        x2a, y2a, x2b, y2b = mode.emailCoordinates
        email = "mailto:mehta.aashav1999@gmail.com"
        if (x2a <= event.x <= x2b) and (y2a <= event.y <= y2b):
            webbrowser.open(email,new="new")

        #Linkedin
        x3a, y3a, x3b, y3b = mode.linkedinCoordinates
        linkedin = "https://www.linkedin.com/in/-a-mehta/"
        if (x3a <= event.x <= x3b) and (y3a <= event.y <= y3b):
            webbrowser.open(linkedin,new="new")

        #finvest
        x4a,y4a,x4b,y4b = mode.finvestCoordinates
        finvest = "https://linktr.ee/Finvest"
        if (x4a <= event.x <= x4b) and (y4a <= event.y <= y4b):
            webbrowser.open(finvest,new="new")


    def redrawAll(mode, canvas):
        canvas.create_image(mode.centerX, mode.centerY,
                            image=ImageTk.PhotoImage(mode.about))
        canvas.create_image(mode.centerHomeX,mode.centerHomeY,
                            image=ImageTk.PhotoImage(mode.homeButton))
        canvas.create_image(mode.centerEmailX, mode.contactY,
                            image=ImageTk.PhotoImage(mode.email))
        canvas.create_image(mode.centerLinkedinX, mode.contactY,
                            image=ImageTk.PhotoImage(mode.linkedin))
        canvas.create_image(mode.centerFinvestX, mode.contactY,
                            image=ImageTk.PhotoImage(mode.finvest))


#used the 112 animation framework for idea of help screen
#link:https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
class learnScreen(Mode):
    def appStarted(mode):
        #background + dimensions
        mode.learnBgd = mode.loadImage("images/learnBgd.png")
        mode.centerX = mode.width // 2
        mode.centerY = mode.height // 2

        #images
        mode.homeButton = mode.loadImage("images/home.png")
        mode.homeButton = mode.scaleImage(mode.homeButton, 3/4)

        #coordinates
        mode.centerHomeX = mode.width/12
        mode.centerHomeY = mode.height/12
        mode.buttonWidth = 150
        mode.buttonHeight = 50

        mode.homeCoordinates = mode.centerHomeX - mode.buttonWidth / 2,\
                          mode.centerHomeY - mode.buttonHeight / 2,\
                          mode.centerHomeX + mode.buttonWidth / 2,\
                          mode.centerHomeY + mode.buttonHeight / 2

    def mousePressed(mode,event):
        #HomeButton
        x1a, y1a, x1b, y1b = mode.homeCoordinates
        if (x1a <= event.x <= x1b) and (y1a <= event.y <= y1b):
            mode.app.setActiveMode(mode.app.splashScreen)


    def redrawAll(mode, canvas):
        canvas.create_image(mode.centerX, mode.centerY,
                            image=ImageTk.PhotoImage(mode.learnBgd))
        canvas.create_image(mode.centerHomeX,mode.centerHomeY,
                            image=ImageTk.PhotoImage(mode.homeButton))



