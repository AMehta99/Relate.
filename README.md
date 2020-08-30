# Relate.

#Description

Relate. is a correlation table app that allows you to create beautiful correlation tables and refer to them at a later time as well. You can create different time periods and test long/short strategies using this software. All you have to do is: 

1. Enter tickers of stocks you want to create a correlation table for 
2. Enter the name of the file you want to store it as 
3. Enter start and end date in yyyy/mm/dd format. 
4. hit correlate! 

#How to run 

open correlation App > open Correlation_Table_app.py and run the file. This will use teh appScreens.py and Market_hedges.py files as well to store the main code. All other files are for storing data, and all correlation tables will be stored as a .png file in the history directory.
Note: The following files need to be in the same folder as Correlation_Table_app.py:
- appScreens.py
- market_Hedges.py
- cmu_112_graphics.py
- history directory
- images directory
- tickers.txt


#Installing Libraries

I have attached the cmu_112_graphics.py file to run the framework and app. This is to be stored in the root depository. These are the other libraries installed and used: 
- import pickle
- import datetime as dt
- import os
- import pandas as pd
- import pandas_datareader.data as web
- import seaborn as sns
- from matplotlib import style
- import random
- import webbrowser


#Shortcuts

I have all of the shortcuts that come with the 112 graphics framework. These shortcuts include screenshots using control s, pausing using control p, and more. These can be found at: 
https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html 
All other shortcuts, or operations may be done through the use of buttons on the screen. 

