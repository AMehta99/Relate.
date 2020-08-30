
#modules to save list of stocks
import pickle     #save data from webscrape

#to scrape data on those stocks and create correlations
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import seaborn as sns

#visualize stocks in table
from matplotlib import style
style.use('ggplot')

#create the app
# CMU Graphics Framework taken from 15-112 Course: Fundamentals of Programming and Computer Science
# https://www.kosbie.net/cmu/fall-19/15-112/notes/notes-animations-part2.html
from cmu_112_graphics import *
import random



#generate random names to store data
def filenamegen(num):
    filename = ""
    for i in range(0,num+1):
        x = random.randint(48,122)
        filename += chr(x)
    return filename


# inspired from pythonprogramming.net
# Link: https://pythonprogramming.net/sp500-company-list-python-programming-for-finance/
def customTables(tickers, filename):
    if (tickers != None) and (filename != None):
        tickerList = []
        for ticker in tickers.split(","):
            ticker = ticker.strip()
            if (".") in ticker:
                newTicker = ticker.replace(".", "-")
                tickerList.append(newTicker)
            else:
                tickerList.append(ticker)
        with open(filename + ".pickle", 'wb') as f:
            pickle.dump(tickerList, f)

        return tickerList


# function by Harrison from pythonprogramming.net:
# https://pythonprogramming.net/sp500-company-price-data-python-programming-for-finance/
def getDataFromYahoo(tickers, directoryName, start, end):
    if (tickers != None) and (directoryName != None) and (start != None) and (end != None):
        if not os.path.exists(directoryName):
            os.makedirs(directoryName)

        startList = list(start.split(","))
        startTime = dt.datetime(int(startList[0]), int(startList[1]), int(startList[2]))
        endList = list(end.split(","))
        endTime = dt.datetime(int(endList[0]), int(endList[1]), int(endList[2]))

        for ticker in tickers:
                if not os.path.exists(directoryName + '/{}.csv'.format(ticker)):
                    df = web.DataReader(ticker, 'yahoo', startTime, endTime)
                    df.to_csv(directoryName + '/{}.csv'.format(ticker))
                else:
                    print("Already Have {}".format(ticker))
        print("Done with data!")
        return tickers

# function adapted from original Harrison from pythonprogramming.net:
# https://pythonprogramming.net/sp500-company-price-data-python-programming-for-finance/
def compileData(filename,directoryName, corrDataFileName):
    if (filename != None) and (directoryName != None) and (corrDataFileName != None):

        with open(filename + ".pickle", "rb") as f:
            tickers = pickle.load(f)

        main_df = pd.DataFrame()

        for count, ticker in enumerate(tickers):
            df = pd.read_csv(directoryName + "/{}.csv".format(ticker))
            df.set_index("Date", inplace=True)
            df.rename(columns = {"Adj Close": ticker},inplace=True)
            df.drop(["Open","High", "Low", "Close", "Volume"], 1, inplace=True)

            if main_df.empty:
                main_df = df
            else:
                main_df = main_df.join(df, how="outer") #joins the columns

            if count % 10 == 0:
                print(count)

        print(main_df.head())
        print("done with joining!")
        main_df.to_csv(corrDataFileName +".csv")


#check the list of entered tickers against all tickers on yahoo finance
def check_tickers(tickers):
    if tickers != None:
        tickerList = []
        for ticker in tickers.split(","):
            ticker = ticker.strip()
            if (".") in ticker:
                newTicker = ticker.replace(".", "-")
                tickerList.append(newTicker)
            else:
                tickerList.append(ticker)
        print(tickerList)

        with open("tickers.txt") as file:
            f = file.read()
            for ticker in tickerList:
                print(ticker)
                if ticker not in f:
                    return False
            return True


class loadScreen(Mode):

    def appStarted(mode):

        #initialize
        mode.centerX = mode.width // 2
        mode.centerY = mode.height // 2
        mode.input = mode.loadImage("images/input.png")
        mode.error = False
        mode.notFound = False

        #inputs
        mode.finalTickers = []
        mode.tickers = ""
        mode.filename = "history/" + filenamegen(5)
        mode.directoryName = "history/" + filenamegen(6)
        mode.corrDataName = ""
        print("appStarted dataname:", mode.corrDataName)
        mode.start = ""
        mode.end = ""


        #buttons
        #all images made using Canva.com
        mode.tickerButton = mode.loadImage("images/tickers.png")
        mode.corrDataNameButton = mode.loadImage("images/corrData.png")
        mode.startdateButton = mode.loadImage("images/startdate.png")
        mode.enddateButton = mode.loadImage("images/enddate.png")
        mode.correlateButton = mode.loadImage("images/correlate.png")
        mode.priorDataButton = mode.loadImage("images/priorData.png")
        mode.homeButton = mode.loadImage("images/home.png")
        mode.buttonWidth = 150
        mode.buttonHeight = 50
        mode.inputY1 = mode.height/3
        mode.inputY2 = mode.height/2
        mode.centerTickerX = mode.width/4
        mode.centerPriorX = mode.width*3/4
        mode.centercorrDataNameX = mode.width/2
        mode.centerstartDateX = mode.width/4
        mode.centerendDateX = mode.width*1/2
        mode.correlateX = mode.width*3/4


        mode.tickerCoordinates = mode.centerTickerX - mode.buttonWidth / 2, \
                               mode.inputY1 - mode.buttonHeight / 2, \
                               mode.centerTickerX + mode.buttonWidth / 2, \
                               mode.inputY1 + mode.buttonHeight / 2
        mode.corrDataNameCoordinates = mode.centercorrDataNameX - mode.buttonWidth / 2, \
                                 mode.inputY1 - mode.buttonHeight / 2, \
                                 mode.centercorrDataNameX + mode.buttonWidth / 2, \
                                 mode.inputY1 + mode.buttonHeight / 2
        mode.priorDataCoordinates = mode.centerPriorX - mode.buttonWidth/2, \
                                    mode.inputY1 - mode.buttonHeight / 2, \
                                    mode.centerPriorX + mode.buttonWidth / 2, \
                                    mode.inputY1 + mode.buttonHeight / 2
        mode.startdateCoordinates = mode.centerstartDateX - mode.buttonWidth / 2, \
                                   mode.inputY2 - mode.buttonHeight / 2, \
                                   mode.centerstartDateX + mode.buttonWidth / 2, \
                                   mode.inputY2 + mode.buttonHeight / 2
        mode.enddateCoordinates = mode.centerendDateX - mode.buttonWidth / 2, \
                                mode.inputY2 - mode.buttonHeight / 2, \
                                mode.centerendDateX + mode.buttonWidth / 2, \
                                mode.inputY2 + mode.buttonHeight / 2
        mode.correlateCoordinates = mode.correlateX - mode.buttonWidth / 2, \
                                mode.inputY2 - mode.buttonHeight / 2, \
                                mode.correlateX + mode.buttonWidth / 2, \
                                mode.inputY2 + mode.buttonHeight / 2
        mode.homeCoordinates = mode.width*9/10 - mode.buttonWidth / 2, \
                                mode.height*12/13 - mode.buttonHeight / 2, \
                                mode.width*9/10 + mode.buttonWidth / 2, \
                                mode.height*12/13 + mode.buttonHeight / 2

    def mousePressed(mode,event):
        #only allow data to be inputed if no errors.
        if mode.error == False and mode.notFound == False:

            #ticker button
            x1a, y1a, x1b, y1b = mode.tickerCoordinates
            if (x1a <= event.x <= x1b) and (y1a <= event.y <= y1b):

                mode.tickers = mode.getUserInput("Enter your stock tickers as comma seperated list")
                if mode.tickers != None:
                    if check_tickers(mode.tickers) == False:
                        mode.error = True


            #prior data button
            x2a,y2a,x2b,y2b = mode.priorDataCoordinates
            if (x2a <= event.x <= x2b) and (y2a <= event.y <= y2b):
                #reload all inputs to avoid errors
                fileName = ""
                loadScreen.corrName = ""
                print("loadScreen.corrName",loadScreen.corrName)
                mode.corrDataName = ""
                mode.start = ""
                mode.end = ""
                mode.filename = ""
                mode.directoryName = ""

                #insert old filename
                fileName = mode.getUserInput("enter name of old file exactly as before")
                mode.corrDataName = fileName
                loadScreen.corrName = mode.corrDataName
                print("mode.corrDataName:", mode.corrDataName)
                print("loadScreen.corrName:", loadScreen.corrName)

            #home button
            x3a, y3a, x3b, y3b = mode.homeCoordinates
            if (x3a <= event.x <= x3b) and (y3a <= event.y <= y3b):
                #reload inputs before leaving screen
                loadScreen.appStarted(mode)
                mode.app.setActiveMode(mode.app.splashScreen)

            #date buttons
            x4a, y4a, x4b, y4b = mode.startdateCoordinates
            if (x4a <= event.x <= x4b) and (y4a <= event.y <= y4b):
                start = mode.getUserInput("enter stock data end date as yyyy,mm,dd")
                if start != None: #avoids cancel button error
                    mode.start = start

            x5a,y5a,x5b,y5b = mode.enddateCoordinates
            if (x5a <= event.x <= x5b) and (y5a <= event.y <= y5b):
                end = mode.getUserInput("enter stock data end date as yyyy,mm,dd")
                if end != None: #avoids cancel button error
                    mode.end = end

            #corr data title button
            x6a, y6a, x6b, y6b = mode.corrDataNameCoordinates
            if (x6a <= event.x <= x6b) and (y6a <= event.y <= y6b):
                corrDataName = mode.getUserInput("Enter title for data set")
                #if corrDataName != None:
                mode.corrDataName = corrDataName
                loadScreen.corrName = mode.corrDataName

            #run button:
            x7a, y7a, x7b, y7b = mode.correlateCoordinates
            if (x7a <= event.x <= x7b) and (y7a <= event.y <= y7b):
                print(mode.start, mode.end)

                #from prior data
                if mode.tickers == "" and mode.corrDataName != None \
                    and mode.start == "" and mode.end == "":
                    if not os.path.exists("history/" + mode.corrDataName + ".csv"):
                        print("got to check not found")
                        mode.notFound = True
                    else:
                        print('using prior data')
                        loadScreen.corrName = mode.corrDataName
                        print(loadScreen.corrName)
                        correlationTable.appStarted(mode)
                        mode.app.setActiveMode(mode.app.correlationTable)


                #restart from scratch: check for criteria filled
                elif mode.tickers == None or mode.corrDataName == None  \
                    or mode.start == None or mode.end == None:
                    print('made an error in inserting data')
                    mode.error = True

                #restart from scratch
                else:
                    try:
                        loadScreen.corrName = mode.corrDataName
                        mode.finalTickers = customTables(mode.tickers, mode.filename)
                        getDataFromYahoo(mode.finalTickers, mode.directoryName, mode.start, mode.end)
                        compileData(mode.filename, mode.directoryName,"history/" + mode.corrDataName)
                        print("using new data to create table")
                        mode.app.setActiveMode(mode.app.correlationTable)

                    except:
                        print("made an error in inserting data")
                        mode.error = True


    def keyPressed(mode,event):
        if mode.error == True:
            mode.error = False #reset it
            loadScreen.appStarted(mode)
            mode.app.setActiveMode(mode.app.loadScreen)
        if mode.notFound == True:
            mode.notFound = False #reset it
            loadScreen.appStarted(mode)
            mode.app.setActiveMode(mode.app.loadScreen)


    def redrawAll(mode, canvas):
        canvas.create_image(mode.centerX, mode.centerY,
                            image=ImageTk.PhotoImage(mode.input))
        canvas.create_image(mode.centerTickerX, mode.inputY1,
                            image=ImageTk.PhotoImage(mode.tickerButton))
        canvas.create_image(mode.centercorrDataNameX, mode.inputY1,
                            image=ImageTk.PhotoImage(mode.corrDataNameButton))
        canvas.create_image(mode.centerstartDateX, mode.inputY2,
                            image=ImageTk.PhotoImage(mode.startdateButton))
        canvas.create_image(mode.centerendDateX, mode.inputY2,
                            image=ImageTk.PhotoImage(mode.enddateButton))
        canvas.create_image(mode.correlateX, mode.inputY2,
                            image=ImageTk.PhotoImage(mode.correlateButton))
        canvas.create_image(mode.centerPriorX, mode.inputY1,
                            image=ImageTk.PhotoImage(mode.priorDataButton))
        canvas.create_image(mode.width*9/10, mode.height*12/13,
                            image=ImageTk.PhotoImage(mode.homeButton))

        if mode.error == True:
            canvas.create_rectangle(mode.width/2 - 120, mode.height/2 - 70, mode.width/2 + 120, mode.height/2 + 70, fill="black", outline="White", width=5)
            canvas.create_text(mode.width/2, mode.height/2, text="  Entered information incorrectly. \n  \n     Check: \n       1. Tickers are valid.  \n       2. dates are formatted properly.\n \n        press any key to restart"
                               , font="Times 14 bold", fill="gold")

        if mode.notFound == True:
            canvas.create_rectangle(mode.width / 2 - 120, mode.height / 2 - 35,
                                    mode.width / 2 + 120, mode.height / 2 + 35,
                                    fill="black", outline="White", width=5)
            canvas.create_text(mode.width / 2, mode.height / 2,
                               text="File not found, \n press any key to go back."
                               , font="Times 16 bold", fill="gold")


class correlationTable(Mode):

    def appStarted(mode):
        print("correlation app has started")

        #initialize
        mode.timerDelay = 1000
        mode.centerX = mode.width // 2
        mode.centerY = mode.height // 2
        mode.cimage = mode.loadImage("images/cimage.png")
        mode.homeButton = mode.loadImage("images/home.png")
        mode.homeButton = mode.scaleImage(mode.homeButton, 3 / 4)
        mode.centerHomeX = mode.width * 11 / 12
        mode.centerHomeY = mode.height * 11.5 / 12
        mode.buttonWidth = 150
        mode.buttonHeight = 50
        mode.homeCoordinates = mode.centerHomeX - mode.buttonWidth / 2, \
                               mode.centerHomeY - mode.buttonHeight / 2, \
                               mode.centerHomeX + mode.buttonWidth / 2, \
                               mode.centerHomeY + mode.buttonHeight / 2

        #inputs
        mode.corrName = mode.app.loadScreen.corrDataName
        print("correlationapp.corrName:",mode.corrName)
        mode.corrData = "history/" + mode.corrName + ".csv"
        mode.plot = "history/" + mode.corrName + ".png"

        #loading plot
        if mode.corrName + ".png" not in os.listdir("history"):
            print(mode.corrName + ".png" + "is being created")
            correlationTable.visualizeData(mode.corrData, "history/" + mode.corrName)

        mode.plotImage = mode.loadImage(mode.plot)
        print("mode.plot:", mode.plot, "got to plot 2 line")
        mode.plot2 = mode.scaleImage(mode.plotImage, .92)





    @staticmethod
    #to create correlation image using data if needed
    def visualizeData(corrData,corrName):

        df = pd.read_csv(corrData)
        df.set_index('Date', inplace=True)
        df_corr = df.corr()  # creates correlation table of dataframe
        data1 = df_corr.values
        column_labels = df_corr.columns
        row_labels = df_corr.index
        f = sns.heatmap(data1, cmap="RdYlGn",annot=True, fmt=".2f",
                        annot_kws={'size':14}, xticklabels=column_labels,
                        yticklabels=row_labels)

        f.get_figure().savefig(corrName + ".png")
        print("saved image")

    #to reload image on each time you enter screen
    def timerFired(mode):
        correlationTable.appStarted(mode)

    #go home
    def mousePressed(mode,event):
        # HomeButton
        x1a, y1a, x1b, y1b = mode.homeCoordinates
        if (x1a <= event.x <= x1b) and (y1a <= event.y <= y1b):
            mode.app.setActiveMode(mode.app.splashScreen)

    def redrawAll(mode, canvas):
        canvas.create_image(mode.centerX, mode.centerY,
                            image=ImageTk.PhotoImage(mode.cimage))

        canvas.create_image(mode.centerX, mode.centerY + 25,
                            image=ImageTk.PhotoImage(mode.plot2))

        canvas.create_image(mode.centerHomeX, mode.centerHomeY,
                            image=ImageTk.PhotoImage(mode.homeButton))







