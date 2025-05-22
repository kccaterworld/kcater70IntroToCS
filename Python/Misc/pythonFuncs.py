#imports
import random
import math
import time
import turtle
import os
import csv
import seaborn as sns
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

#Globals
#Boolean to run or not run test cases
testRun = True
indent = "    "
lineBreak = "\n<br>"
newLine = '''
'''
#Multiline for HTML Webpages, it gets replaced by the actual content by certain functions
pageMultiline = '''<!DOCTYPE html>
<html>
    <head> _HEAD_
    </head>
    <body>
    _BODY_
    </body>
</html>'''

#An alphabetically sorted list of every color from the turtle module
#Requires turtlecolors.csv to be in the same directory as Python file
with open("turtcolors.csv", "r") as colors:
    colors = sorted(list({color for color in colors.read().split("\n")}),key=str.lower)

#Helper Functions

def freqWords(data):
    wordFreq = {}
    for word in data:
        if word in wordFreq:
            wordFreq[word] += 1
        else:
            wordFreq[word] = 1
    return wordFreq


#matplotlib helper functions
#makeScatterGraph(title: str = "Title",
#              figSize: tuple = (15, 9),
#              xLabel: str = "X-Axis Label",
#              yLabel: str = "Y-Axis Label",
#              xData: list = [1,2,3,4,5],
#              yData: list = [1,2,3,4,5],
#              size: int = 10,
#              color: str = "black",
#              xTickRot: int = 0,
#              filename: str = "plotPic",
#              legend: str = "Legend",
#              legLoc: str = 'upper left',
#              locator: int = 1,
#              show: bool = True) -> None
#Title -> String
#figSize -> Tuple of ints
#xLabel -> String
#yLabel -> String
#xData -> List of ints
#yData -> List of ints
#size -> Int
#color -> String
#xTickRot -> Int
#filename -> String
#legend -> String
#legLoc -> String
#locator -> Int
#show -> Bool
#Creates a scatter plot with the specified parameters.
#If show is True, it will display the plot.
#If save is True, it will save the plot as a png with the given filename.
#If the filename already exists, it will be overwritten.
def makeScatterGraph(title: str = "Title",
              figSize: tuple = (15, 9),
              xLabel: str = "X-Axis Label",
              yLabel: str = "Y-Axis Label",
              xData: list = [1,2,3,4,5],
              yData: list = [1,2,3,4,5],
              size: int = 10,
              color: str = "black",
              xTickRot: int = 0,
              filename: str = "plotPic",
              legend: str = "Legend",
              legLoc: str = 'upper left',
              locator: int = 1,
              show: bool = True,
              save: bool = True) -> None:
    fig, ax = plt.subplots(figsize=figSize)
    ax.set_title(title )
    ax.scatter(xData, yData, c=color, s=size)
    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    ax.set_xticks(xData)
    ax.set_xticklabels(xData, rotation=xTickRot, ha='right')
    ax.set_yticks(yData)
    ax.set_yticklabels(yData)
    ax.xaxis.set_major_locator(MultipleLocator(locator))
    ax.legend([legend], loc=legLoc)
    if save:
        plt.savefig(f"{filename}.png")
    if show:
        plt.show()

#makeLinePlot(xAxis: list = [],
#             yAxis: list = [],
#             title: str = "Title",
#             xLabel: str = "X-Axis Label",
#             yLabel: str = "Y-Axis Label",
#             color: str = "black",
#             marker: str = "o",
#             linestyle: str = "-",
#             markersize: int = 0,
#             label: str = "Line",
#             alpha: float = 1,
#             linewidth: int = 1,
#             markeredgecolor: str = "black",
#             markeredgewidth: int = 1,
#             markerfacecolor: str = "black",
#             show: bool = True,
#             xTicksRot: int = 0,
#             yTicksRot: int = 0,
#             legLoc: str = "upper left",
#             gridStyle: str = "--",
#             gridAlpha: int = 0.5,
#             grid: bool = True,
#             xMultipleLocator: int = 1,
#             yMultipleLocator: int = 1,
#             saveFig: bool = True,
#             figName:str = "") -> None:
#Creates a line plot with the given parameters.
#xAxis: list of x values
#yAxis: list of y values
#title: title of the plot
#xLabel: label for the x-axis
#yLabel: label for the y-axis
#color: color of the line
#marker: marker style for the points
#linestyle: style of the line
#markersize: size of the markers
#label: label for the line in the legend
#alpha: transparency of the line
#linewidth: width of the line
#markeredgecolor: color of the marker edge
#markeredgewidth: width of the marker edge
#markerfacecolor: color of the marker face
#show: whether to show the plot
#xTicksRot: rotation of the x-axis ticks
#yTicksRot: rotation of the y-axis ticks
#legLoc: location of the legend
#gridStyle: style of the grid lines
#gridAlpha: transparency of the grid lines
#grid: whether to show the grid
#xMultipleLocator: interval for the x-axis ticks
#yMultipleLocator: interval for the y-axis ticks
#saveFig: whether to save the figure
#figName: name of the saved figure file
#Returns: None
#It also uses the MultipleLocator class from the ticker module to set the tick intervals.
#It saves the figure as a PNG file if saveFig is True.
#It shows the plot if show is True.
def makeLinePlot(xAxis: list = [],
                 yAxis: list = [],
                 title: str = "Title",
                 xLabel: str = "X-Axis Label",
                 yLabel: str = "Y-Axis Label",
                 color: str = "black",
                 marker: str = "o",
                 linestyle: str = "-",
                 markersize: int = 0,
                 label: str = "Line",
                 alpha: float = 1,
                 linewidth: int = 1,
                 markeredgecolor: str = "black",
                 markeredgewidth: int = 1,
                 markerfacecolor: str = "black",
                 show: bool = True,
                 xTicksRot: int = 0,
                 yTicksRot: int = 0,
                 legLoc: str = "upper left",
                 gridStyle: str = "--",
                 gridAlpha: int = 0.5,
                 grid: bool = True,
                 xMultipleLocator: int = 1,
                 yMultipleLocator: int = 1,
                 saveFig: bool = True,
                 figName:str = "") -> None:
    import matplotlib.pyplot as plt
    from matplotlib.ticker import MultipleLocator
    plt.plot(xAxis,
         yAxis,
         color=color,
         marker=marker,
         linestyle=linestyle,
         markersize=markersize,
         label=label,
         alpha=alpha,
         linewidth=linewidth,
         markeredgecolor=markeredgecolor,
         markeredgewidth=markeredgewidth,
         markerfacecolor=markerfacecolor,)
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.xticks(xAxis, rotation=xTicksRot, ha='right')
    plt.yticks(yAxis, rotation=yTicksRot, ha='right')
    plt.legend(loc=legLoc)
    if grid:
        plt.grid(linestyle=gridStyle, alpha=gridAlpha)
    plt.gca().xaxis.set_major_locator(MultipleLocator(xMultipleLocator))
    plt.gca().yaxis.set_major_locator(MultipleLocator(yMultipleLocator))
    if saveFig:
        plt.savefig(f"{figName}.png")
    if show:
        plt.show()

#myRot90(array: list = [[]],
#        numTimes: int = 1,
#        axes: list = []) -> list
#array -> list of lists
#numTimes -> int
#axes -> list of ints
#Rotates the array 90 degrees counter-clockwise numTimes times.
#If numTimes is 0, it will return the original array.
#If numTimes is 1, it will return the array rotated 90 degrees counter-clockwise.
def myRot90(array: list = [[]],
            numTimes: int = 1,
            axes: list = []) -> list:
    if numTimes == 1:
        return [list(row) for row in zip(*array)]
    else:
        myRot90([list(row) for row in zip(*array)], numTimes - 1, axes)

#mean(vals: tuple = ()) -> float
#vals -> tuple of numbers
#Returns the mean of the numbers in vals.
#If vals is empty, it will return 0.0.
def mean(vals: tuple = ()) -> float:
    if len(vals) == 0:
        return 0.0
    sum = 0
    for number in vals:
        sum += number
    return float(sum / len(vals))

#stripInner(list,item) -> list
#text -> list of strings
#item -> list of strings
#Removes all instances of item from text
#Returns the modified text as a string
def stripInner(text: str = "",
               item: str = ""):
    data = list(text)
    for thing in item:
        while thing in data:
            data.remove(thing)
    return " ".join(data)

#File I/O functions

#writePage(path, content) -> None
#page -> string
#content -> string
#Writes the content to the specified path, creating a new file if it doesn't exist.
#If the file already exists, it will be overwritten.
def writePage(path, content):
    with open(path, "w") as file:
        file.write(content)

#readCSV(path, rotate) -> list
#path -> string
#rotate -> int
#Reads a CSV file and returns a list of lists, where each inner list is a row in the CSV file.
def readCSV(path: str = "",
            rotate: int = 0) -> list:
    with open(path, "r") as file:
        dataTable = [row.split(",") for row in file.read().split("\n")]
    if rotate > 0:
        return myRot90(dataTable, rotate)
    else:
        return dataTable
    
def runTestCases(run: bool = True):
    #It will only run test cases is run == True
    if run:
        #Test Cases here
        
        #Prints out end message
        print("\n\nTests Finished")

runTestCases(testRun)