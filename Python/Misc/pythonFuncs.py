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
pageMultiline = '''
<!DOCTYPE html>
<html>
    <head> _HEAD_
    </head>
    <body>
    _BODY_
    </body>
</html>
'''

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


#HTML/CSS helper functions

#makeHead(title) -> string
#title -> string
#css -> list of lists, optimized for buildCSSBlock()
def titleCSS(title:str = "Title"):
    titleCSSMultiline = f'''
    \t<title> {title} </title>
    \t<style> _CSS_ </style>
    '''
    titleCSSMultiline = titleCSSMultiline.replace("_CSS_",buildCSSFull())
    return titleCSSMultiline

#buildCSSBlock(cssElement,cssProperty,cssValue) -> string
#cssElement -> string
#cssProperty -> string
#cssValue -> string
#Creates a CSS block for element(s) cssElement, with respective properties and values.
#If inputs are invalid it will not render
def buildCSSBlock(cssElement: str = "Example Tag",
                  cssProperty: list = ["Example Property"],
                  cssValue: list = ["Example Value"]):
    cssMultiline = '''_ELEMENT_ {
        _PROPERTIES_
	}
	'''
    properties = ""
    cssMultiline = cssMultiline.replace("_ELEMENT_",cssElement)
    for i in range(len(cssProperty)):
        properties += f"    " + cssProperty[i] + ":" + cssValue[i] + ";"
    cssMultiline = cssMultiline.replace("_PROPERTIES_",properties)
    return cssMultiline

#buildCSSFull() -> string
def buildCSSFull():
    cssFull = ""
    cssFull += buildCSSBlock("Example Tag",["Example Property"],["Example Value"])
    return cssFull

#buildMeta(charset,description,keywords,author,viewport) -> string
#charset -> string
#description -> string
#keywords -> string
#author -> string
#viewport -> string
#Creates a meta tag for the HTML page, with the specified charset, description, keywords, author, and viewport.
def buildMeta(charset,description,keywords,author,viewport):
   return f'''\t<meta charset="{charset}">
    \t<meta name="description" content="{description}">
    \t<meta name="keywords" content="{keywords}">
    \t<meta name="author" content="{author}">
    \t<meta name="viewport" content="{viewport}">'''

#buildHeadLinks(rel,type,href) -> string
#rel -> string
#type -> string
#href -> string
#Creates a link tag for the HTML page, with the specified rel, type, and href.
#rel: stylesheet, icon, etc.
#type: text/css, image/x-icon, etc.
def buildHeadLinks(rel,type,href):
    return f'''\t<link rel="{rel}" type="{type}" href="{href}">'''

#buildHeader(tag,content,*styles) -> string
#tag -> string
#content -> string
#Generates a simple HTML block (generalized version of makePara)
def buildHeader(tag,content):
    return f'''\t<{tag}> {str(content)} </{tag}>'''

#buildLink(ref,content,newTab) -> string
#ref -> string
#content -> string
#newTab -> bool
#Creates a link tag for the HTML page, with the specified ref, content, and newTab.
#ref: the link to go to, content: the text to display, newTab: whether to open in a new tab or not
#newTab: True = new tab, False = same tab, None = same tab
def buildLink(ref,content,newTab: bool = False):
    if newTab == True:
        nT = '''target="_blank"'''
    else:
        nT = ""
    return f'''\n\t<a href="https://www.{ref}" {nT}> {content} </a>'''

#buildPara(text) -> string
#text -> string
#Generates an HTML paragraph with conents text
def buildPara(text):
    return f"\n\t<p> {str(text)} </p>" 

#buildTable(caption,header,body,footer) -> string
#caption -> string
#header -> list of lists
#body -> list of lists
#footer -> list of lists
#Creates HTML table with caption Caption, using header, body, and footer as such.
#header, body, footer: main list is all data, each inner list is a row, each list value is a collumn for that row
def buildTable(caption,header,body,footer):
            tableMultiline = '''\n\t<table>
            <caption> _CAPTION_ </caption>
            <thead> _HEAD_
            </thead>
            <tbody> _BODY_
            </tbody>
            <tfoot> _FOOT_
            </tfoot>
        </table>\n'''
            multHead = ""
            multBody = ""
            multFoot = ""
            for item in header:
                multHead += "\n\t\t<tr>"
                for cell in item:
                    multHead += "<th>" + str(cell) + "</th>"
                multHead += "</tr>"
            for item in body:
                multBody += "\n\t\t<tr>"
                for cell in item:
                    multBody += "<td>" + str(cell) + "</td>"
                multBody += "</tr>"
            for item in footer:
                multFoot += "\n\t\t<tr>"
                for cell in item:
                    multFoot += "<td>" + str(cell) + "</td>"
                multFoot += "</tr>"
            tableMultiline = tableMultiline.replace("_CAPTION_",caption)
            tableMultiline = tableMultiline.replace("_HEAD_",multHead)
            tableMultiline = tableMultiline.replace("_BODY_",multBody)
            tableMultiline = tableMultiline.replace("_FOOT_",multFoot)
            return tableMultiline

#buildList(title,items,type) -> string
#title -> string
#items -> list
#type -> string
#creates HTML list of specified type using title Title, containing item list entries
def buildList(title,items,type):
    list = '\n\t<'+type+'> ' +  str(title)
    for i in range(len(items)):
        list += '\n\t    <li> ' + str(items[i]) + '</li>'
    list += '\n\t</'+type+'>'
    return list

#genPageHead() -> string
#Creates the head of the HTML page, including title, CSS, meta tags, and links.
def genPageHead():
    pageHead = ""
    #Example of how to add to pageHead
    pageHead += ""
    #Example title and CSS commands (IMPORTANT)
    pageHead += titleCSS("Example Title","ExampleCSS")
    #Adding meta tags (IMPORTANT)
    pageHead += indent + newLine + buildMeta("UFT-8","Example Description","Example Keywords","Example Author","width=device-width, initial-scale=1.0",)
    #Adding links (IMPORTANT)
    pageHead += indent + newLine + buildHeadLinks("stylesheet","text/css","style.css")
    pageHead += indent + newLine + buildHeadLinks("icon","image/x-icon","favicon.ico")    
    return pageHead

#genPageBody() -> string
#Creates the body of the HTML page, including headers, paragraphs, tables, and lists.
def genPageBody():
    pageBody = ""
    #Example of how to add to pageBody (include newLine)
    pageBody += ""
    #Example Header
    pageBody += buildHeader("h1","Example Header!")
    pageBody += buildLink("youtube.com","Youtube",True)
    #Example Paragraph
    pageBody += newLine + buildPara("HIIIIIII")
    #Example table of how rows and collumns work in each section. (SECTION)(ROWNUM)(COLNUM) SECTION: [H(header),B(body),F(footer)]
    pageBody += newLine + buildTable("Example Table",[["HR1C1","HR1C2"],["HR2C1","HR2C2"]],[["BR1C1","BR1C2"],["BR2C1","BR2C2"]],[["FR1C1","FR1C2"],["FR2C1","FR2C2"]])
    #Example lists
    pageBody += buildList("Example Ordered List",["First","Second","Third"],"ol")
    pageBody += newLine + buildList("Example Unordered List",["Item","Item","Item"],"ul")
    return pageBody

#genPage() -> string
#Creates the entire HTML page, including head and body.
#This is the main function that will be called to generate the page.
def genPage():
    MPage = pageMultiline.replace("_HEAD_",genPageHead())
    MPage = MPage.replace("_BODY_",genPageBody())
    return MPage


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